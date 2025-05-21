import openai
import os
# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

class OpenAIFileManager:
    @staticmethod
    def upload_file():
        filepath = input("Enter path of file to upload: ")
        if not os.path.isfile(filepath):
            print("File does not exist.")
            return
        purpose = input("Enter purpose user_data | vision | fine-tune | batch (default = 'user_data'): ") or "user_data"
        try:
            with open(filepath, "rb") as f:
                response = openai.files.create(file=f, purpose=purpose)
            print(f"Uploaded: ID = {response.id} | Name = {response.filename}")
        except Exception as e:
            print(f"Error uploading file: {e}")
    
    @staticmethod
    def list_files():
        try:
            files = openai.files.list()
            if not files.data:
                print("No files found.")
                return
            print("\nAvailable Files:")
            for f in files.data:
                print(f"ID: {f.id} | Name: {f.filename} | Purpose: {f.purpose} | Status: {f.status}")
        except Exception as e:
            print(f"Error listing files: {e}")

    @staticmethod
    def retrieve_file_content():
        file_id = input("Enter file ID: ")
        try:
            content = openai.files.content(file_id).read().decode('utf-8')
            print("\nFile Content:")
            print(content)
        except Exception as e:
            print(f"Error retrieving content: {e}")
    
    @staticmethod
    def download_file():
        file_id = input("Enter file ID: ")
        destination = input("Enter destination path (e.g., output.jsonl): ")
        try:
            file_content = openai.files.content(file_id)
            with open(destination, "wb") as f:
                f.write(file_content.read())
                print(f"File downloaded to {destination}")
        except Exception as e:
            print(f"Error downloading file: {e}")
    
    @staticmethod
    def delete_file():
        file_id = input("Enter file ID to delete: ")
        try:
            response = openai.files.delete(file_id)
            print(f"Deleted file: {file_id} | Status: {response.deleted}")
        except Exception as e:
            print(f"Error deleting file: {e}")

def main():
    manager = OpenAIFileManager()
    while True:
        print("\n===== OpenAI File Manager Menu =====")
        print("1. Upload a File")
        print("2. List All Files")
        print("3. Retrieve File Content")
        print("4. Download a File")
        print("5. Delete a File")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            manager.upload_file()
        elif choice == '2':
            manager.list_files()
        elif choice == '3':
            manager.retrieve_file_content()
        elif choice == '4':
            manager.download_file()
        elif choice == '5':
            manager.delete_file()
        elif choice == '6':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number bet2ween 1 and 6.")


if __name__ == "__main__":
    main()


