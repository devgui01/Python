"""
Progress Tracker - Track your learning journey

Usage:
    python progress.py mark 001      # Mark exercise 001 as complete
    python progress.py status        # Show overall progress
    python progress.py reset         # Reset all progress
"""

import json
import os
from datetime import datetime
from pathlib import Path


class ProgressTracker:
    """Track learning progress across exercises and projects"""
    
    def __init__(self):
        self.progress_file = "tools/progress_data.json"
        self.data = self.load_progress()
    
    def load_progress(self):
        """Load progress from file"""
        if os.path.exists(self.progress_file):
            with open(self.progress_file, 'r') as f:
                return json.load(f)
        return {
            "exercises": {},
            "projects": {},
            "quizzes": {},
            "started_at": datetime.now().isoformat(),
            "last_activity": datetime.now().isoformat()
        }
    
    def save_progress(self):
        """Save progress to file"""
        self.data["last_activity"] = datetime.now().isoformat()
        os.makedirs(os.path.dirname(self.progress_file), exist_ok=True)
        with open(self.progress_file, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def mark_exercise_complete(self, exercise_id):
        """Mark an exercise as complete"""
        exercise_id = exercise_id.zfill(3)
        self.data["exercises"][exercise_id] = {
            "completed": True,
            "completed_at": datetime.now().isoformat(),
            "attempts": self.data["exercises"].get(exercise_id, {}).get("attempts", 0) + 1
        }
        self.save_progress()
        print(f"✓ Exercise {exercise_id} marked as complete!")
    
    def mark_project_complete(self, project_id):
        """Mark a project as complete"""
        self.data["projects"][project_id] = {
            "completed": True,
            "completed_at": datetime.now().isoformat()
        }
        self.save_progress()
        print(f"✓ Project {project_id} marked as complete!")
    
    def get_status(self):
        """Get progress summary"""
        total_exercises = 50  # Expected total
        completed_exercises = len([e for e in self.data["exercises"].values() if e.get("completed")])
        
        total_projects = 10
        completed_projects = len([p for p in self.data["projects"].values() if p.get("completed")])
        
        print("\n" + "="*50)
        print("📊 YOUR LEARNING PROGRESS")
        print("="*50)
        
        # Exercises
        print(f"\n📝 Exercises: {completed_exercises}/{total_exercises}")
        progress_bar = "█" * int((completed_exercises/total_exercises)*20) + "░" * (20 - int((completed_exercises/total_exercises)*20))
        print(f"[{progress_bar}] {completed_exercises/total_exercises*100:.1f}%")
        
        if self.data["exercises"]:
            print("\nCompleted Exercises:")
            for ex_id, data in sorted(self.data["exercises"].items()):
                if data.get("completed"):
                    print(f"  ✓ #{ex_id} - {data['completed_at'][:10]}")
        
        # Projects
        print(f"\n🚀 Projects: {completed_projects}/{total_projects}")
        progress_bar = "█" * int((completed_projects/total_projects)*20) + "░" * (20 - int((completed_projects/total_projects)*20))
        print(f"[{progress_bar}] {completed_projects/total_projects*100:.1f}%")
        
        # Stats
        print(f"\n📈 Statistics:")
        print(f"  Started: {self.data['started_at'][:10]}")
        print(f"  Last Activity: {self.data['last_activity'][:10]}")
        
        # Recommendations
        print(f"\n💡 Next Steps:")
        if completed_exercises < 10:
            print("  → Complete more beginner exercises (001-020)")
        elif completed_exercises < 30:
            print("  → Try intermediate exercises (011-030)")
        elif completed_exercises < 50:
            print("  → Challenge yourself with advanced exercises (031-050)")
        else:
            print("  → Start a capstone project!")
        
        print("\n" + "="*50)
    
    def reset(self):
        """Reset all progress"""
        confirm = input("Are you sure you want to reset all progress? (y/n): ")
        if confirm.lower() == 'y':
            self.data = {
                "exercises": {},
                "projects": {},
                "quizzes": {},
                "started_at": datetime.now().isoformat(),
                "last_activity": datetime.now().isoformat()
            }
            self.save_progress()
            print("✓ Progress reset successfully!")
        else:
            print("✗ Reset cancelled")


def main():
    import sys
    
    tracker = ProgressTracker()
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python progress.py mark 001    # Mark exercise complete")
        print("  python progress.py status      # Show progress")
        print("  python progress.py reset       # Reset progress")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "mark" and len(sys.argv) > 2:
        tracker.mark_exercise_complete(sys.argv[2])
    elif command == "status":
        tracker.get_status()
    elif command == "reset":
        tracker.reset()
    else:
        print("Unknown command. Use: mark, status, or reset")
        sys.exit(1)


if __name__ == "__main__":
    main()
