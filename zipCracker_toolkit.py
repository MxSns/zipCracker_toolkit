import argparse, string, os, zipfile

# Lets parse some args

parser = argparse.ArgumentParser(description="Iterate in a text to find some potential passwords, attempt to crack the zip password then")

parser.add_argument("zip", help="The path to the zip file")
parser.add_argument("-l", "--wordlist", required=True, help="The password list")
args = parser.parse_args()


def extract_wordlist (input_path, output_path):
    with open(input_path, 'r', encoding='UTF-8') as f:
        text = f.read()

    tokens = text.split()

    passwords = []

    for token in tokens:
        stripped = token.strip(string.punctuation)
        if len(stripped) > 4:
                passwords.append(stripped)

    with open(output_path, 'w', encoding='UTF-8') as f:
        for password in passwords:
            f.write(f"{password}\n")

def extract_archive(zip_path, output_folder, wordlist_path="none"):

    if not os.path.exists(zip_path):
        raise FileNotFoundError(f"Zip file not found: {zip_path}")

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    try:
        with zipfile.ZipFile(zip_path) as zf:
            zf.extractall(output_folder)
        print("Extracted without password")
        return
    except RuntimeError as e:
        # Check if error due to passwd requirement
        if 'encrypted' not in str(e).lower() and 'password' not in str(e).lower():
            raise e
        print("Password required; attempting to crack using wordlist.")
    except zipfile.BadZipFile:
        raise ValueError(f"Invalid zip file: {zip_path}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error opening zip: {str(e)}")
    else:
        # If no exception (successful no-password extract)
        extracted_files = os.listdir(output_folder)
        print(f"Extracted  files : {extracted_files}")
        return

    if wordlist_path is None:
        raise FileNotFoundError(f"Wordlist required not found: {wordlist_path}")

    with open(wordlist_path, 'r', encoding='UTF-8') as f:
        passwords = [line.strip() for line in f if line.strip()]

    if not passwords:
        raise ValueError("Wordlist is empty")

    for pw in passwords:
        try:
            with zipfile.ZipFile(zip_path) as zf:
                zf.extractall(output_folder, pwd=pw.encode('UTF-8'))
            print(f"Successfully extracted with password: {pw}")
            extracted_files = os.listdir(output_folder)
            print(f"Extracted files : {extracted_files}")
            return
        except RuntimeError as e:
            # Continue if bad password
            if 'bad password' in str(e).lower() or 'password required':
                continue
            else:
                raise e
        except Exception as e:
            raise RuntimeError(f"Unexpected error during extraction with {pw}: {str(e)}")
    raise ValueError("No password from wordlist worked.")
        


extract_wordlist(args.wordlist, "wordlist.txt")
extract_archive(args.zip, "zip_content", "wordlist.txt")
