from .models import Equipement, Character
from django.shortcuts import render, get_object_or_404, redirect
from .forms import MoveForm
from django.contrib import messages  # Importer messages pour afficher des messages d'erreur

def character_list(request):
    equipements = Equipement.objects.all()
    characters = Character.objects.all()
    return render(request, 'animalerie/character_list.html', {
        'equipements': equipements,
        'characters': characters,
    })

def character_detail(request, id_character):
    character = get_object_or_404(Character, id_character=id_character)
    form = MoveForm()

    if request.method == 'POST':
        form = MoveForm(request.POST)
        
        if form.is_valid():
            nouveau_lieu = form.cleaned_data['lieu']
            ancien_lieu = get_object_or_404(Equipement, id_equip=character.lieu.id_equip)


            if nouveau_lieu.disponibilite == "occupé" and nouveau_lieu.id_equip !="sofa":
                messages.error(request, f"{nouveau_lieu.id_equip} est occupé, impossible d'y aller.")
                return render(request, 'animalerie/character_detail.html', {
                    'character': character,
                    'lieu': character.lieu,
                    'form': form
                })
        
            # Vérifications de disponibilité et de condition d'état
            if nouveau_lieu.id_equip == "sofa":
                if character.etat != "fatigué":
                    messages.error(request, f"{character.id_character} n'est pas fatigué et ne peut pas aller sur le sofa.")
                    return render(request, 'animalerie/character_detail.html', {
                        'character': character,
                        'lieu': character.lieu,
                        'form': form
                    })
                else:
                    character.etat = "affamé"
                    ancien_lieu.disponibilite = "libre"

            elif nouveau_lieu.id_equip == "gamelles":
                if character.etat != "affamé":
                    messages.error(request, f"{character.id_character} n'est pas affamé et ne peut pas aller à la gamelle.")
                    return render(request, 'animalerie/character_detail.html', {
                        'character': character,
                        'lieu': character.lieu,
                        'form': form
                    })
                else:
                    character.etat = "joueur"
                    ancien_lieu.disponibilite = "libre"
                    nouveau_lieu.disponibilite = "occupé"

            elif nouveau_lieu.id_equip == "mes genoux":
                if character.etat not in ["fatigué", "joueur"]:
                    messages.error(request, f"{character.id_character} n'est ni fatigué ni joueur et ne peut pas aller sur les genoux.")
                    return render(request, 'animalerie/character_detail.html', {
                        'character': character,
                        'lieu': character.lieu,
                        'form': form
                    })
                else:
                    character.etat = "affamé"
                    ancien_lieu.disponibilite = "libre"
                    nouveau_lieu.disponibilite = "occupé"


            elif nouveau_lieu.id_equip == "Plant d'herbe à chats":
                if character.etat != "joueur":
                    messages.error(request, f"{character.id_character} n'est pas joueur et ne peut pas aller sur les plants d'herbe à chat.")
                    return render(request, 'animalerie/character_detail.html', {
                        'character': character,
                        'lieu': character.lieu,
                        'form': form
                    })
                else:
                    character.etat = "fatigué"
                    ancien_lieu.disponibilite = "libre"
                    nouveau_lieu.disponibilite = "occupé"


            # Mise à jour du personnage
            character.lieu = nouveau_lieu
            character.save()
            ancien_lieu.save()
            nouveau_lieu.save()

            # Rediriger après succès
            return redirect('character_detail', id_character=id_character)

    return render(request, 'animalerie/character_detail.html', {
        'character': character,
        'lieu': character.lieu,
        'form': form
    })
