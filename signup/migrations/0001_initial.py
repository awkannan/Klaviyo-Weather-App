# Generated by Django 2.0.1 on 2018-01-27 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tagline', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('address', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('body_text', models.TextField()),
                ('pub_date', models.DateField()),
                ('mod_date', models.DateField()),
                ('n_comments', models.IntegerField()),
                ('n_pingbacks', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('authors', models.ManyToManyField(to='signup.Author')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signup.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date', models.DateField()),
                ('weather', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signup.City')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='WeatherSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('location', models.CharField(choices=[('', 'Select nearest city...'), ('Albuquerque,New Mexico', 'Albuquerque, New Mexico'), ('Anaheim,California', 'Anaheim, California'), ('Anchorage,Alaska', 'Anchorage, Alaska'), ('Arlington,Texas', 'Arlington, Texas'), ('Atlanta,Georgia', 'Atlanta, Georgia'), ('Aurora,Colorado', 'Aurora, Colorado'), ('Austin,Texas', 'Austin, Texas'), ('Bakersfield,California', 'Bakersfield, California'), ('Baltimore,Maryland', 'Baltimore, Maryland'), ('Baton Rouge,Louisiana', 'Baton Rouge, Louisiana'), ('Birmingham,Alabama', 'Birmingham, Alabama'), ('Boise,Idaho', 'Boise, Idaho'), ('Boston,Massachusetts', 'Boston, Massachusetts'), ('Buffalo,New York', 'Buffalo, New York'), ('Chandler,Arizona', 'Chandler, Arizona'), ('Charlotte,North Carolina', 'Charlotte, North Carolina'), ('Chesapeake,Virginia', 'Chesapeake, Virginia'), ('Chicago,Illinois', 'Chicago, Illinois'), ('Chula Vista,California', 'Chula Vista, California'), ('Cincinnati,Ohio', 'Cincinnati, Ohio'), ('Cleveland,Ohio', 'Cleveland, Ohio'), ('Colorado Springs,Colorado', 'Colorado Springs, Colorado'), ('Columbus,Ohio', 'Columbus, Ohio'), ('Corpus Christi,Texas', 'Corpus Christi, Texas'), ('Dallas,Texas', 'Dallas, Texas'), ('Denver,Colorado', 'Denver, Colorado'), ('Detroit,Michigan', 'Detroit, Michigan'), ('Durham,North Carolina', 'Durham, North Carolina'), ('El Paso,Texas', 'El Paso, Texas'), ('Fort Wayne,Indiana', 'Fort Wayne, Indiana'), ('Fort Worth,Texas', 'Fort Worth, Texas'), ('Fremont,California', 'Fremont, California'), ('Fresno,California', 'Fresno, California'), ('Garland,Texas', 'Garland, Texas'), ('Gilbert,Arizona', 'Gilbert, Arizona'), ('Glendale,Arizona', 'Glendale, Arizona'), ('Greensboro,North Carolina', 'Greensboro, North Carolina'), ('Henderson,Nevada', 'Henderson, Nevada'), ('Hialeah,Florida', 'Hialeah, Florida'), ("Honolulu,Hawai'i", "Honolulu, Hawai'i"), ('Houston,Texas', 'Houston, Texas'), ('Indianapolis,Indiana', 'Indianapolis, Indiana'), ('Irvine,California', 'Irvine, California'), ('Irving,Texas', 'Irving, Texas'), ('Jacksonville,Florida', 'Jacksonville, Florida'), ('Jersey City,New Jersey', 'Jersey City, New Jersey'), ('Kansas City,Missouri', 'Kansas City, Missouri'), ('Laredo,Texas', 'Laredo, Texas'), ('Las Vagas,Nevada', 'Las Vagas, Nevada'), ('Las Vegas,Nevada', 'Las Vegas, Nevada'), ('Lexington,Kentucky', 'Lexington, Kentucky'), ('Lincoln,Nebraska', 'Lincoln, Nebraska'), ('Long Beach,California', 'Long Beach, California'), ('Los Angeles,California', 'Los Angeles, California'), ('Louisville,Kentucky', 'Louisville, Kentucky'), ('Lubbock,Texas', 'Lubbock, Texas'), ('Madison,Wisconsin', 'Madison, Wisconsin'), ('Memphis,Tennessee', 'Memphis, Tennessee'), ('Mesa,Arizona', 'Mesa, Arizona'), ('Miami,Florida', 'Miami, Florida'), ('Milwaukee,Wisconsin', 'Milwaukee, Wisconsin'), ('Nashville,Tennessee', 'Nashville, Tennessee'), ('New York,New York', 'New York, New York'), ('Newark,New Jersey', 'Newark, New Jersey'), ('Norfolk,Virginia', 'Norfolk, Virginia'), ('Oakland,California', 'Oakland, California'), ('Oklahoma,Oklahoma', 'Oklahoma, Oklahoma'), ('Omaha,Kansas', 'Omaha, Kansas'), ('Omaha,Louisiana', 'Omaha, Louisiana'), ('Omaha,Minnesota', 'Omaha, Minnesota'), ('Omaha,Nebraska', 'Omaha, Nebraska'), ('Orlando,Florida', 'Orlando, Florida'), ('Philadelphia,Pennsylvania', 'Philadelphia, Pennsylvania'), ('Phoenix,Arizona', 'Phoenix, Arizona'), ('Pittsburgh,Pennsylvania', 'Pittsburgh, Pennsylvania'), ('Plano,Texas', 'Plano, Texas'), ('Portland,Oregon', 'Portland, Oregon'), ('Raleigh,North Carolina', 'Raleigh, North Carolina'), ('Reno,Nevada', 'Reno, Nevada'), ('Riverside,California', 'Riverside, California'), ('Sacramento,California', 'Sacramento, California'), ('Saint Paul,Minnesota', 'Saint Paul, Minnesota'), ('San Antonio,Texas', 'San Antonio, Texas'), ('San Bernardino,California', 'San Bernardino, California'), ('San Diego,California', 'San Diego, California'), ('San Francisco,California', 'San Francisco, California'), ('San Jose,California', 'San Jose, California'), ('Santa Ana,California', 'Santa Ana, California'), ('Scottsdale,Arizona', 'Scottsdale, Arizona'), ('Seattle,Washington', 'Seattle, Washington'), ('St. Louis,Missouri', 'St. Louis, Missouri'), ('St. Petersburg,Florida', 'St. Petersburg, Florida'), ('Stockton,California', 'Stockton, California'), ('Tampa,Florida', 'Tampa, Florida'), ('Toledo,Ohio', 'Toledo, Ohio'), ('Tucson,Arizona', 'Tucson, Arizona'), ('Tulsa,Oklahoma', 'Tulsa, Oklahoma'), ('Virginia Beach,Virginia', 'Virginia Beach, Virginia'), ('Washington,District of Columbia', 'Washington, District of Columbia'), ('Winston–Salem,North Carolina', 'Winston–Salem, North Carolina')], max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signup.Question'),
        ),
    ]
