<a id="top"></a>

#

<h1 align="center">
Contabo Snapshot Automation
</h1>

<p align="center"> 
  <kbd>
<img src="https://raw.githubusercontent.com/r0xd4n3t/contabo-snapshot-automation/main/img/contabo.png"></img>
  </kbd>
</p>
Automated Contabo cloud instance snapshot management using Python. Easily create and delete snapshots for data protection.

<p align="center">
<img src="https://img.shields.io/github/last-commit/r0xd4n3t/contabo-snapshot-automation?style=flat">
<img src="https://img.shields.io/github/stars/r0xd4n3t/contabo-snapshot-automation?color=brightgreen">
<img src="https://img.shields.io/github/forks/r0xd4n3t/contabo-snapshot-automation?color=brightgreen">
</p>

# Contabo Snapshot Automation

Automate snapshot management for Contabo cloud instances using Python. This script allows you to create and delete snapshots for your Contabo cloud instances, ensuring data protection and efficient resource management.

## Prerequisites

Before using this script, make sure you have the following prerequisites:

- Contabo API credentials (CLIENT_ID, CLIENT_SECRET, API_USER, API_PASSWORD)
- Python 3.x installed
- Required Python packages (install using `pip install -r requirements.txt`)

## Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/r0xd4n3t/contabo-snapshot-automation.git
   cd contabo-snapshot-automation

2. Create a config.conf file and add your Contabo API credentials:
   ```json
   {
    "TELEGRAM_BOT_TOKEN": "your_telegram_bot_token",
    "TELEGRAM_CHAT_ID": "your_telegram_chat_id",
    "CLIENT_ID": "your_client_id",
    "CLIENT_SECRET": "your_client_secret",
    "API_USER": "your_api_user",
    "API_PASSWORD": "your_api_password"
    }
    ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt

4. Run the script or you can put in cronjob:
   ```bash
   python contabo_snapshot.py
   ```
   Example: To set up a cron job to run your contabo_snapshot.py script every 15 days, you can use the cron scheduling syntax to specify the timing
   ```bash
   0 0 */15 * * /usr/bin/python3.10 /user/contabo_backup/contabo_snapshot.py
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to submit a pull request to add new adlists or make improvements.

---


<p align="center"><a href=#top>Back to Top</a></p>
