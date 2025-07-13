
import time
import sys
import random
import os

def type_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_bar(task="Processing", length=30):
    bar = ''
    for i in range(length):
        bar += random.choice(['█', '▓', '▒', '░'])
        sys.stdout.write(f"\r>>> {task}: [{bar:<{length}}]")
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def access_terminal():
    type_effect(">>> Authenticating identity...")
    loading_bar("Identity Match")
    time.sleep(0.5)
    type_effect(">>> Access Level: SHADOW-7")
    time.sleep(0.5)
    type_effect(">>> Welcome, K.I.D.")
    time.sleep(1)

    while True:
        command = input("K.I.D@c0de666:~$ ").strip().lower()

        if command == "help":
            print("\nAvailable Commands:")
            print("- scan_target")
            print("- decrypt_logs")
            print("- override_system")
            print("- exit\n")

        elif command == "scan_target":
            type_effect(">>> Scanning global nodes...")
            loading_bar("Node Scan")
            type_effect(">>> Result: 3 weak targets found.")
        
        elif command == "decrypt_logs":
            type_effect(">>> Decrypting classified logs...")
            loading_bar("Decryption")
            type_effect(">>> Log 001: Project OMEGA initiated.")
            type_effect(">>> Log 002: Agent K.I.D. still undetected.")
            type_effect(">>> Log 003: - no system is safe -")

        elif command == "override_system":
            type_effect(">>> Launching override protocol...")
            loading_bar("System Override")
            type_effect(">>> SYSTEM BREACH SUCCESSFUL.")
            type_effect(">>> You are now inside.")

        elif command == "exit":
            type_effect(">>> Terminating session...")
            break

        else:
            type_effect(">>> Unknown command. Type 'help'.")

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    type_effect(">>> Establishing secure connection...")
    loading_bar("Booting Terminal")
    access_terminal()
