## Dovecot Setup

### SSL/TLS
#### IMAP (993)
Inside the file **10-master.conf** you need to uncomment the part related to the imaps (secure imap) and comment the part related to imap:
```py
service imap-login {
  inet_listener imap {
    # port = 143
  }
  inet_listener imaps {
    port = 993
    ssl = yes
  }
}
```
Inside the **10-ssl.conf** file there must be this kind of configuration:
```py
# SSL/TLS support: yes, no, required. <doc/wiki/SSL.txt>
ssl = yes

ssl_cert = </etc/dovecot/private/dovecot.pem
ssl_key = </etc/dovecot/private/dovecot.key
```

Inside **10-auth.conf** there is the authentication mechanism used and the include of another file:
```py
auth_mechanisms = plain
!include auth-system.conf.ext
```
The **auth-system.conf.ext** file is important in defining how Dovecot handles authentication and user lookups, which are key components for any mail server. Specially, it governs the way users are authenticated when accessing email services (such as IMAP/POP3) and how user data is retrieved.
```py
# This specifies how Dovecot translates email addresses into usernames for authentication
# %n refers to the "username" part of the email address, so it will remove the domain
auth_username_format = %n

# The passdb section defines the password database that Dovecot will use to authenticate users
passdb {
  driver = passwd-file
  args = /etc/dovecot/users
}

# The userdb section defines how Dovecot looks up user information, such as home directories, 
# UIDs (user IDs), GIDs (group IDs), and any other attributes Dovecot might need
userdb {
  driver = passwd-file
  args = /etc/dovecot/users
}
```

### Logs Dovecot
Inside the file **10-logging.conf** there are some lines that must be added:
```bash
# Log path
log_path = /var/log/dovecot.log
# Log file to use for informational messages. Defaults to log_path.
info_log_path = /var/log/dovecot-info.log
# Log file to use for debug messages. Defaults to info_log_path.
debug_log_path = /var/log/dovecot-debug.log

# Log unsuccessful authentication attempts and the reasons why they failed.
auth_verbose = yes

# Enable mail process debugging. This can help you figure out why Dovecot isn't finding your mails.
mail_debug = yes
```
To see the logs:
```bash
# Inside the email_server
tail -f var/log/dovecot-info.log
```
