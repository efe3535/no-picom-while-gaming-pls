from time import sleep
from psutil import process_iter
from os import system

def main():
    picom_running = False
    picom_killed = False

    while True:
        try:
            running = process_iter(["name"])
            
            for is_picom_running in running:
                if "picom" in is_picom_running.info["name"]: 
                    picom_running = True
                    break

            for process in running:
                if process.info["name"] == "steam" and picom_running:
                    print("Steam is running. Closing your picom.")
                    if(picom_killed == False):
                        system("killall -9 picom")
                        picom_killed = True
                    else:
                        # Picom is killed, start waiting for Steam to restart Picom then.
                        while True:
                            running_list = []
                            running_2 =  process_iter(["name"])
                            for _ in running_2:
                                running_list.append(_.info["name"])  
                            if("steam" in running_list):
                                pass
                            
                            else:
                                print("Starting picom as steam is not running")
                                import subprocess
                                subprocess.Popen(["picom","--daemon"])
                                exit(0)
            sleep(3)

        except KeyboardInterrupt:
            print("Dude chill, I'm stopping now ok...")
            exit(0)

if __name__ == "__main__" :
    main()
