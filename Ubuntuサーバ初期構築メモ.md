sudo apt update
sudo apt upgrade
systemctl status sshd
sudo apt install openssh-server
networkctl status
ssh-keygen -lv -f /etc/ssh/ssh_host_ecdsa_key.pub

sudo apt install language-pack-ja
sudo localectl set-locale 'LANG=ja_JP.utf8'
date

sudo apt install manpages-ja manpages-ja-dev

.bashrc
[[ $TERM == 'linux ]] && LANG=en_US.utf-8

sudo timedatectl set-timezone 'Asia/Tokyo'
date
timedatectl status

networkctl
ip a

# UFW (Uncomplicated FireWall)
sudo ufw allow OpenSSH
sudo ufw enable
sudo ufw status
sudo ss -nltp | grep ssh

sudo nano /etc/rsyslog.d/20-ufw.conf
「# & stop」のコメントを外して有効に。
sudo systemctl restart rsyslog.service

