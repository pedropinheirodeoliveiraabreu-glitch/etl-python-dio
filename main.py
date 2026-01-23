from extract import extract
from transform import transform
from load import load

def main():
    data = extract()
    data = transform(data)
    load(data)

if __name__ == "__main__":
    main()
