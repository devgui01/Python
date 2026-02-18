import importlib
import tiktoken

tokenizer = tiktoken.get_encoding("o200k_base")
text = (
    " Hello Subscribe ? <|endoftext|> DartStorm"
)

integers = tokenizer.encode(text, allowed_special={"<|endoftext|>"})
print(integers)
strings = tokenizer.decode(integers)
print(strings)
new = tokenizer.encode("Qwer Tyhj JJyy GHG", allowed_special={"<|endoftext|>"})
print(f"Encoded : {new}")

