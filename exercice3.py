
def decomposer(secondes):
    secondes_par_années = 3600 * 24 * 365
    secondes_par_semaines = 3600 * 24 * 7
    secondes_par_jours = 3600 * 24
    secondes_par_heures = 3600
    secondes_par_minutes = 60


    # TODO: Assigner à la variable "annees" le nombre d'années
    annees = int(secondes/secondes_par_années)
    reste_annees = secondes - annees*secondes_par_années

    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    semaines = int(reste_annees/secondes_par_semaines)
    reste_semaines = reste_annees - semaines*secondes_par_semaines

    # TODO: Assigner à la variable "jours" le nombre de jours restants
    jours = int(reste_semaines/secondes_par_jours)
    reste_jours = reste_semaines - jours*secondes_par_jours

    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    heures = int(reste_jours/secondes_par_heures)
    reste_heures = reste_jours - heures*secondes_par_heures

    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    minutes = int(reste_heures/secondes_par_minutes)
    reste_minutes = reste_heures - minutes*secondes_par_minutes

    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes = int(reste_minutes)

    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(annees ,semaines ,jours ,heures ,minutes ,secondes)

    return (f'{annees} années, {semaines} semaines, {jours} jours, {heures} heures, {minutes} minutes et {secondes} secondes ')

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))
