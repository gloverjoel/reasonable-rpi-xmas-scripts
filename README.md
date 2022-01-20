# reasonable-rpi-xmas-scripts
Script edits for 3D RGB Xmas Tree for Raspberry Pi

sudo apt update && upgrade
sudo apt install python3-pip

    Create a service via:
    sudo systemctl --force --full edit <YOUR-NAME>.service
    And paste

    [Unit]
    Description=<(Optional) Description of your project>
    After=network.target

    [Service]
    ExecStart=<YOUR-PYTHON-PATH> <PATH-TO-YOUR-SCRIPT>.py

    [Install]
    WantedBy=multi-user.target

    Save it and reload all Systemd services via
    sudo systemctl daemon-reload
    Enable autostart on boot of your new service:\
    sudo systemctl enable <YOUR-NAME>.service

