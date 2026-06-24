import json, logging

# Setup basic logging to a file
logging.basicConfig(filename='app.log', level=logging.INFO)

# Custom Exception
class EmptyNameError(Exception): pass

def main():
    # Demonstrating try / except / else / finally
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
        logging.warning("File missing or corrupt. Starting fresh.")
    else:
        logging.info("Data loaded successfully.")
    finally:
        print("--- Startup Complete ---")

    while True:
        c = input("\n1.Add 2.View 3.Exit : ").strip()
        
        if c == '1':
            try:
                name = input("Name: ").strip()
                if not name: 
                    raise EmptyNameError("Name cannot be blank!") # Trigger custom error
                
                data.append({"name": name, "phone": input("Phone: ").strip()})
                
                with open('data.json', 'w') as f: 
                    json.dump(data, f)
                    
                print("✅ Saved!")
                logging.info(f"Added {name}")
                
            except EmptyNameError as e:
                print(f"❌ Error: {e}")
                logging.error(e)
                
        elif c == '2':
            print(data if data else "No contacts yet.")
            
        elif c == '3':
            break

if __name__ == "__main__": 
    main()