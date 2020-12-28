DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "awx",
        'USER': "awx",
        'PASSWORD': "awxpass",
        'HOST': "postgres",
        'PORT': "5432",
    }
}

BROADCAST_WEBSOCKET_SECRET = "N3JGZmltamQ3dWtENU1RYnBhbEJBOnFJT0JQZGs2NzVZdkd0dEdlbmdSYnhhQWR3V2lZYVNnWEtrUjJKNDQ3ZktkZVA4dTlkRmFGLUxCLTFPMXh3LXhVVUs1X0w1TEZhSHpicFAtQmFieU5Fc0E3V00sT3l1SDB6NTRDLFVQdFU="
