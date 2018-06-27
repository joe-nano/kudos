# Deploy with supervisor

```bash
# Move the conf to where it can be read
cp kudos.conf /etc/supervisor/conf.d/kudos.conf
# Edit the file for correct paths
sudo vim /etc/supervisor/conf.d/kudos.conf

# Create the log folders
sudo mkdir /var/log/kudos

# Set appropriate permissions
chown leswing:leswing /var/log/kudos

# Edit the runserver.sh to set PATH correctly
vim runserver.sh

# Reread and restart supervisor
sudo supervisorctl reread
sudo supervisorctl update
```
