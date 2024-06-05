## Generar secret key
```
python manage.py shell
```
```
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

## collectstatic
```
python manage.py collectstatic --noinput
```

# Node
```
npm init -y
```
```
npm install tailwindcss
```
```
npx tailwindcss init
```
```
npm run tailwind
```