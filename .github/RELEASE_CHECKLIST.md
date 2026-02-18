# Release Checklist

## Pre-Release

- [ ] All tests passing
- [ ] Code formatted (Black, Ruff)
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] Version number updated

## Release Steps

1. **Create Release Branch**
   ```bash
   git checkout -b release/v1.0.0
   ```

2. **Update Version**
   - Update version in pyproject.toml
   - Update CHANGELOG.md
   - Commit changes

3. **Create Tag**
   ```bash
   git tag -a v1.0.0 -m "Release v1.0.0 - Initial Release"
   git push origin v1.0.0
   ```

4. **Create Release on GitHub**
   - Go to Releases page
   - Click "Create new release"
   - Select tag v1.0.0
   - Add release notes
   - Publish release

5. **Merge to Main**
   ```bash
   git checkout main
   git merge release/v1.0.0
   git push origin main
   ```

## Post-Release

- [ ] Verify release on GitHub
- [ ] Check GitHub Packages
- [ ] Update documentation
- [ ] Announce release
