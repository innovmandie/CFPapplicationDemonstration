# Generated by Django 3.2.18 on 2024-03-18 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CFPapp', '0019_auto_20240317_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posta1_c2',
            name='A1_C2',
            field=models.CharField(choices=[('Degre_1', 'Degré 1 J’évalue la fiabilité d’une source, crédibilité et réputation).'), ('Degre_2', 'Degré 2 Je sélectionne les sources les plus pertinentes au regard de mes missions et de la stratégie de ma structure.'), ('Degre_3', 'Degré 3 J’évalue la complétude de ma veille. Pour compléter ma veille j’identifie de nouveaux acteurs.'), ('Degre_4', 'Degré 4 Je conseille les décideurs sur la recherche de prestataires et d’outils performants de veille.'), ('N_S_P', 'Ne se prononce pas')], default='Degre_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='posta2_c1',
            name='A2_C1',
            field=models.CharField(choices=[('Degre_1', 'Degré 1 J’ai mis en œuvre la démarche de diagnostic lors de mon année probatoire.'), ('Degre_2', 'Degré 2 Je repère les enjeux, attentes et besoins du commanditaire.'), ('Degre_3', 'Degré 3 J’organise ma démarche de diagnostic : identification des acteurs clés, choix des outils d’investigations.'), ('Degre_4', 'Degré 4 Je suis un acteur ressource pour le réseau en capacité d’accompagner mes pairs sur la structuration et la démarche de diagnostic.'), ('N_S_P', 'Ne se prononce pas')], default='Degre_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='posta3_c1',
            name='A3_C1',
            field=models.CharField(choices=[('Degre_1', 'Degré 1 Je connais les éléments qui positionnent une structure sur le marché de la formation professionnelle.'), ('Degre_2', 'Degré 2 Je sais positionner mon organisation dans le cadre réglementaire et législatif de la formation professionnelle.'), ('Degre_3', 'Degré 3 Je m’approprie les analyses existantes.'), ('Degre_4', 'Degré 4 Je suis un acteur ressource du réseau en capacité de former mes pairs.'), ('N_S_P', 'Ne se prononce pas')], default='Degre_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='posta3_c3',
            name='A3_C3',
            field=models.CharField(choices=[('Degre_1', 'Degré 1 Je prends connaissance des comptes-rendus des différentes instances.'), ('Degre_2', 'Degré 2 Je participe aux instances de concertation en apportant des éléments d’analyse.'), ('Degre_3', 'Degré 3 Je contribue à l’ordre du jour des instances de concertation.'), ('Degre_4', 'Degré 4 Dans les instances de concertation à l’interne, je suis consulté sur des orientations.'), ('N_S_P', 'Ne se prononce pas')], default='Degre_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='posta4_c1',
            name='A4_C1',
            field=models.CharField(choices=[('Degre_1', 'Degré 1 Je connais les décideurs, le circuit décisionnel de ma structure, les instances s’y référant.'), ('Degre_2', 'Degré 2 J’identifie le décideur concerné au regard de la situation requérant un conseil.'), ('Degre_3', 'Degré 3 Je m’empare du besoin de conseil, en caractérisant le périmètre, le degré d’urgence.'), ('Degre_4', 'Degré 4 J’anticipe des situations qui pourraient être sensibles et impactantes pour le développement de ma structure.'), ('N_S_P', 'Ne se prononce pas')], default='Degre_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='posta4_c2',
            name='A4_C2',
            field=models.CharField(choices=[('Degre_1', 'Degré 1 Je connais des méthodes et des outils d’analyse.'), ('Degre_2', 'Degré 2 J’utilise une méthode et les outils d’analyse nécessaires à la bonne compréhension.'), ('Degre_3', 'Degré 3 A partir de mon analyse de la situation ou de la demande, j’envisage les pistes de réponses.'), ('Degre_4', 'Degré 4 Je suis un acteur ressource pour le réseau pour accompagner mes pairs sur les méthodes.'), ('N_S_P', 'Ne se prononce pas')], default='Degre_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='posta4_c3',
            name='A4_C3',
            field=models.CharField(choices=[('Degre_1', 'Degré 1 Je connais les outils de communication adaptés au conseil : synthèse, note d’opportunité, rapport, etc.'), ('Degre_2', 'Degré 2 Je choisis les outils de communication adaptés aux décideurs.'), ('Degre_3', 'Degré 3 Je propose à l’écrit ou à l’oral un contenu synthétique pour être lu ou entendu par les décideurs.'), ('Degre_4', 'Degré 4 A la demande des décideurs, je rédige et je présente un rapport circonstancié.'), ('N_S_P', 'Ne se prononce pas')], default='Degre_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='posta5_c1',
            name='A5_C1',
            field=models.CharField(choices=[('Degre_1', 'Degré 1 Je connais les différentes instances de mon territoire, leurs rôles et leur fonctionnement.'), ('Degre_2', 'Degré 2 Je participe aux échanges, aux réunions et aux groupes de travail du territoire.'), ('Degre_3', 'Degré 3 J’adapte ma posture et mes propos en fonction de mes interlocuteurs et des instances.'), ('Degre_4', 'Degré 4 Je suis sollicité en qualité d’expert de la formation professionnelle.'), ('N_S_P', 'Ne se prononce pas')], default='Degre_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='posta5_c2',
            name='A5_C2',
            field=models.CharField(choices=[('Degre_1', 'Degré 1 Je distingue les 3 voies de formation professionnelle. Je m’informe en interne sur les missions.'), ('Degre_2', 'Degré 2 J’identifie sur mon territoire l’offre de formations.'), ('Degre_3', 'Degré 3 J’explique la mission de service public de l’éducation nationale.'), ('Degre_4', 'Degré 4 Je suis un acteur ressource pour le réseau en capacité d’analyser et d’harmoniser les pratiques de promotion de l’organisation.'), ('N_S_P', 'Ne se prononce pas')], default='Degre_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='posta5_c3',
            name='A5_C3',
            field=models.CharField(choices=[('Degre_1', 'Degré 1 Je connais les acteurs socio-économiques de mon territoire.'), ('Degre_2', 'Degré 2 Je construis un réseau de partenaires socio-économiques.'), ('Degre_3', 'Degré 3 Je suis un interlocuteur reconnu et sollicité par les acteurs socio-économiques.'), ('Degre_4', 'Degré 4 Je suis à l’initiative de rencontres partenariales sur un projet donné.'), ('N_S_P', 'Ne se prononce pas')], default='Degre_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='posta6_c1',
            name='A6_C1',
            field=models.CharField(choices=[('Degre_1', 'Degré 1 Je connais les éléments constitutifs d’une politique commerciale d’une organisation.'), ('Degre_2', 'Degré 2 J’apporte des éléments d’analyse permettant l’évolution de la politique commerciale'), ('Degre_3', 'Degré 3 Je contribue à la définition des objectifs de la politique commerciale.'), ('Degre_4', 'Degré 4 Je suis un acteur ressource pour le réseau en capacité d’accompagner les équipes en place et transmettre une méthodologie.'), ('N_S_P', 'Ne se prononce pas')], default='Degre_1', max_length=20),
        ),
    ]
