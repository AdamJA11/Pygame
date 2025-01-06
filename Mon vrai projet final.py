# pas oublier de taper pip install pygame et pip install pygame_gui dans le terminal avant de lancer
import pygame

import pygame_gui
from pygame_gui.elements import UIButton
import sys
import math
import random
pygame.init()
X, Y = 400, 300
angle = 0
vaisseau = None
vaisseau2 = None
vitesse = 0
Verif2 = True
coef = 1
angle2 = 0
angle3 = 0
Xcircle = random.randint(0, 390)
Ycircle = random.randint(0,590)
cometeV = random.randint(0, 4)
movement_sens = random.randint(-1, 1)
projectileV = 5.5
Xprojectile = 400
Yprojectile = 300
projectiles = []
projectile_cooldown= 0
pivot = 400//2,300//2
compteurluck = 0
nombre_asteroides = 3
compteur_asteroides = nombre_asteroides + compteurluck
score = 0
score_text = None
font = pygame.font.Font(None, 36)
Verif3 = True
Verif1 = True
vaisseau_gost = None
angle_gost = 0
x_gost = 250
y_gost =  250
pivot_gost= (x_gost, y_gost)
msg_text = None
cooldown_msg = None

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
manager = pygame_gui.UIManager((800, 600))


        
            


def main():
    global Verif1, X, Y, angle, vaisseau, vaisseau2, vitesse, Verif2, coef, angle2, angle3, \
           Xcircle, Ycircle, cometeV, movement_sens, projectileV, Xprojectile, Yprojectile, \
           projectiles, projectile_cooldown, pivot, nombre_asteroides, compteur_asteroides, \
           score, score_text, font, asteroides, image, Verif3, compteurluck, vaisseau_gost,x_gost, y_gost,pivot_gost,angle_gost,msg_text, cooldown_msg


    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    manager = pygame_gui.UIManager((800, 600))
    
    def reset_game():
        global Verif1, X, Y, angle, vitesse, Verif2, coef, angle2, angle3, \
            Xcircle, Ycircle, cometeV, movement_sens, projectileV, Xprojectile, Yprojectile, \
            projectiles, projectile_cooldown, pivot, nombre_asteroides, compteur_asteroides, \
            score, score_text, asteroides, compteurluck,vaisseau_gost,x_gost, y_gost,pivot_gost,angle_gost,msg_text, cooldown_msg

        X, Y = 400, 300
        angle = 0
        vitesse = 0
        coef = 1
        angle2 = 0
        Xcircle = random.randint(0, 390)
        Ycircle = random.randint(0, 590)
        movement_sens = random.randint(-1, 1)
        projectile_cooldown = 0
        pivot = 400 // 2, 300 // 2
        score = 0
        score_text = None
        compteurluck = 0
        nombre_asteroides = 3
        asteroides = creation_asteroides(nombre_asteroides)
        compteur_asteroides = 3*nombre_asteroides + compteurluck
        angle_gost = 0
        x_gost = 250
        y_gost =  250
        pivot_gost= (x_gost, y_gost)
        vaisseau_gost = None
        msg_text = None
        cooldown_msg = None
        
        
    def transition():
        
        max_radius = 400
        min_radius = 40
        current_radius = max_radius
        radius_decrement = 10
        alpha = 0
        loading_text = font.render("Chargement...", True, (0, 0, 0))
        text_rect = loading_text.get_rect(center=(400, 300))

        while current_radius > min_radius:
            timelaps = random.randint(250, 775 )
            pygame.time.delay(timelaps)
            screen.fill((0, 0, 0))  # Remplit l'écran avec la couleur de fond
            pygame.draw.circle(screen, (255, 255, 255), (400, 300), int(current_radius))
            screen.blit(loading_text, text_rect)
            pygame.draw.arc(screen, (255, 255, 255), (100, 100, 600, 400), 0, math.radians(alpha), 5)
            pygame.display.flip()
            current_radius -= radius_decrement
            alpha += 15
    def acceuil(image_path):
        global Verif1
        image = pygame.image.load(image_path).convert_alpha()
    
        # Redimensionner l'image à la taille spécifiée (800x600)
        image = pygame.transform.scale(image, (800, 600))
        
        # Vérifier si l'image a été chargée correctement
        if image and Verif1 == True:
            # Afficher l'image à l'emplacement (0, 0) sur l'écran
            screen.blit(image, (0, 0))

    def oeil():
        global X, Y
        radiuseye = 15
        angleBeta = math.atan((X )/ (Y))
        xeye = ((30 - radiuseye)*math.sin(angleBeta)) + (50)
        yeye = ((30 - radiuseye)*math.cos(angleBeta)) + (75/2)
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((xeye-radiuseye-5), (yeye-radiuseye-5), (2*radiuseye + 10), (2*radiuseye+ 10)))
        pygame.draw.circle(screen, (255,255,255), (xeye,yeye), radiuseye,1 )
        

    
        

    def creation_du_contour_oeil():
        global X,Y
        beta = 360
        oeil()
        pygame.draw.arc(screen, (255, 255, 255), (0, 0,100, 75), 0, math.radians(beta), 3)
        pygame.draw.circle(screen, (255,255,255), (50,37), 30,1 )
        
        #tourne selon un mauvais centre de rotation 
    


        


    def creation_de_button(x, y, text1):
        return UIButton(relative_rect=pygame.Rect(x, y, 100, 50),
                        text=text1,
                        manager=manager)
    #cette fonction permet de cree un bouton dans les texte et les coordonnes peuvent 
    #choisi a sa guise 
    
    # cree un bouton start 
    

    start_Button = creation_de_button(350, 275, "Start")

    def direction_du_mouvement(direction):
        global vaisseau
        global vaisseau2
        global angle
        if direction == "gauche":    
            return  pygame.transform.rotate(vaisseau, angle)  
        if direction == "droite":
            return   pygame.transform.rotate(vaisseau, angle) 
        #permet de controler la rotation du vaisseau selon qu il va a gauche ou a droite
        
    def creation_de_comete ():
        global Xcircle
        global Ycircle
        return pygame.draw.circle(screen, (255, 255,255), (Xcircle, Ycircle), 20, 2)
        #cree une comete avec des valeurs par defaut

    def mouvement_de_comete ():
        global Xcircle
        global Ycircle
        global movement_sens
        Xcircle = Xcircle + (movement_sens*cometeV)
        Ycircle = Ycircle + (movement_sens*cometeV)
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 800, 600))
        return creation_de_comete()
    def creation_de_projectile(coordonnesA, coordonnesB):
        projectile1 = 0
        
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(coordonnesA- 20, coordonnesB - 20, 20, 20))
        return projectile1 == pygame.draw.circle(screen, (255, 255, 255), (coordonnesA,coordonnesB ), 5)
    #fonction pour cree un projectile selon des coordonnes A et B choisi 

    def collision_detection(rect1, rect2):
        return rect1.colliderect(rect2)
    #une fonction pour detecter les collision 

    def creation_asteroides(nombre_asteroides):
        asteroides = []
        global compteurluck
        
        
        for _ in range(nombre_asteroides):
            luck_coef = random.randint(0,6)
           
            asteroides.append({
                'x': random.randint(0, 800),
                'y': random.randint(0, 600),
                'radius': 35,
                'direction': random.randint(0, 360),
                'specialcase' : False,
                'speed': 2,
                'divisible': True  # Ajoutez la propriété 'divisible'
            })
            if luck_coef == 3:
                compteurluck = compteurluck + 1
                asteroides.append({
                'x': random.randint(0, 800),
                'y': random.randint(0, 600),
                'radius': 50,
                'direction': random.randint(0, 360),
                'specialcase' : True,
                'speed': 2,
                'divisible2': True  # Ajoutez la propriété 'divisible'
               
                })
                
                
                
                

        return asteroides 
    
    # cette fonction va venir ajouter a un dictionnaire des coordonnes aleatoire, une direction d'angle aleatoire 
    #et d autre donnes qui nous servirons par la suite et renvoyer les astroides le dictionnaire 

    def diviser_asteroide(asteroide):
        global asteroides
        asteroides.remove(asteroide)

        # Divisez l'astéroïde uniquement s'il est marqué comme divisible
        if asteroide['specialcase'] == False:
            if asteroide['divisible'] == True:
                nouveau_rayon = asteroide['radius'] // 2
                for _ in range(2):
                    asteroides.append({
                        'x': asteroide['x'] + random.randint(-10, 10),
                        'y': asteroide['y'] + random.randint(-10, 10),
                        'radius': nouveau_rayon,
                        'direction': random.randint(0, 360),
                        'specialcase' : False,
                        'speed': asteroide['speed'] * 0.5,
                        'divisible': False  # Marquez l'astéroïde fils comme non divisible
                    })
    #cette fonction si utiliser va enlever l'asteroide et regarder si cellui rempli la condition divisible 
    # si oui il ajouterra 2 asteroides 2 fois plus petit au dictionnaire asteroides       



    asteroides = creation_asteroides(nombre_asteroides)
    # vient ajouter liee ce dictionaire a une variable asetroides 
    compteur_asteroides = 3*nombre_asteroides + (compteurluck)
    #compte les asteroides sur le terrain petit ou pas 
    while True:

        time_delta = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                
                if event.ui_element == start_Button:
                    
                    start_Button.kill()
                    
                    Verif1 = False
                                        
                    vaisseau = pygame.image.load("vaisseauA.jpg").convert_alpha()
                    vaisseau = pygame.transform.scale(vaisseau, (80,80))
                    vaisseau2 = pygame.image.load("vaisseauA.jpg").convert_alpha()
                    vaisseau2 = pygame.transform.scale(vaisseau2, (80, 80))
                    pivot = (X, Y)
                    #vient initialiser les valeurs du debut du jeu 
                    
        

        

        manager.process_events(event)
        
        

        
        
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 800, 600))
        
        if Verif1 == False:
            creation_du_contour_oeil()
        
        
                    
                    
                
    
        if event.type == pygame.KEYUP and event.key == pygame.K_UP :
            angle2 = angle
        #au moment ou le joueur lache le bouton K_UP ca capture langle 
        if pygame.key.get_pressed()[pygame.K_UP] == True  and Verif1 == False :
            
            if angle != angle2 and coef < 1:
                coef = coef + 0.5
            #si angle differents de celui capture augmente un coef ce qui a pour effet d'aumenter la vitesse
        
            Y = Y - vitesse*math.cos(math.radians(angle))*coef

            X = X - vitesse*math.sin(math.radians(angle))*coef
            pivot = (X, Y)
            # si le joueur appuie sur K_UP ca cree un vecteur  et renitialiser la posiont du pivot de centre
            # de rotation

            if vitesse <4:
                vitesse = vitesse + 0.1
                # acceleation 
            Verif2 = False #initialise une variable pour engendrer par la suite la gravite 
        if Verif2 == False and pygame.key.get_pressed()[pygame.K_UP] == False :
            if coef > 0 and angle != angle2:
                coef = coef - 0.5
        # si Verif2 = False sa veut dire que le bouton K_UP avait ete appuye mais si en plus le bouton K_UP actuellement 
        # est pas appuye genere un mouvement dans la direction de l'angle appuye 

            Y = Y - (vitesse - coef)*math.cos(math.radians(angle2))
            X = X - (vitesse- coef)*math.sin(math.radians(angle2))
            pivot = (X, Y)
            #initialise le centre de rotation pivot(x,y)
            
        if X > 800 + 25:
                X = 0-25
                pivot = (X, Y)
            # Si le vaisseau dépasse le bord gauche, il réapparaît à droite
        elif X < 0- 25:
                X = 800 + 25
                pivot = (X, Y)

            # Si le vaisseau dépasse le bord bas, il réapparaît en haut
        if Y > 600+ 25:
                Y = 0-25
                pivot = (X, Y)
            # Si le vaisseau dépasse le bord haut, il réapparaît en bas
        elif Y < 0- 25:
                Y = 600+ 25
                pivot = (X, Y)

            
        if pygame.key.get_pressed()[pygame.K_LEFT] and Verif1 == False:
            angle = angle + 5
            vaisseau2 = pygame.transform.rotate(vaisseau, angle)
            pivot = (X, Y)
            # ne fait que rotater le vaisseau vers la droite et reactualise le pivot de rotation 
            

        if pygame.key.get_pressed()[pygame.K_RIGHT] and Verif1 == False:
            
            angle = angle - 5
            vaisseau2 = pygame.transform.rotate(vaisseau, angle )
            pivot = (X, Y)
            # ne fait que rotater le vaisseau vers la droite et reactualise le pivot de rotation 


        if angle < 0:
            angle += 360
        elif angle >= 360:
            angle -= 360
        # si l angle est trop grand renitialise pour faciliter la comprhension de calcule 
        
        

        
        
        if pygame.key.get_pressed()[pygame.K_SPACE] == True and Verif1 == False and projectile_cooldown <= 0:
            
            projectiles.append({'x': X, 'y': Y, 'angle': angle, 'lifetime': 100})  # 100 est un exemple, ajustez selon vos besoins
            #si la touche espace est appuye va venir incrire des valeur propore au vaisseau et une duree de vie du projectiles
            projectile_cooldown = 50  # Temps de recharge du projectile

        
        

        
        
        for asteroide in asteroides:
            if asteroide['specialcase'] == True:
                pygame.draw.circle(screen, (50, 50, 255), (asteroide['x'], asteroide['y']), asteroide['radius'], 2)
            else:
                pygame.draw.circle(screen, (255, 255, 255), (asteroide['x'], asteroide['y']), asteroide['radius'], 2)
            
            vaisseau_rect = pygame.Rect(X,Y, 10, 10)
            
            
            if asteroide['specialcase'] == True:
                asteroide_rect2 = pygame.Rect(asteroide['x'] - asteroide['radius'], asteroide['y'] - asteroide['radius'], 2 * asteroide['radius'], 2 * asteroide['radius'])
            else:
                asteroide_rect = pygame.Rect(asteroide['x'] - asteroide['radius'], asteroide['y'] - asteroide['radius'], 2 * asteroide['radius'], 2 * asteroide['radius'])
            if vaisseau_rect.colliderect(asteroide_rect):
                for projectile in projectiles:
                    projectiles.remove(projectile)
                reset_game()
                break  # Arrêtez de vérifier les autres astéroïdes après la première collision détectée
        
            
            
            # Vérifier la collision avec chaque projectile
            for projectile in projectiles:
                projectile_rect = pygame.Rect(projectile['x'] - 5, projectile['y'] - 5, 10, 10)
                if collision_detection(projectile_rect, asteroide_rect):
                    diviser_asteroide(asteroide)
                    projectiles.remove(projectile)
                    if type(score) != str:
                        score += 50
                    compteur_asteroides = compteur_asteroides - 1
                    score_text = font.render(f"Score: {score}", True, (255, 255, 255))

                    break
            if asteroide["specialcase"] == True:
                for projectile in projectiles:
                    projectile_rect = pygame.Rect(projectile['x'] - 5, projectile['y'] - 5, 10, 10)
                    if collision_detection(projectile_rect, asteroide_rect2):
                        diviser_asteroide(asteroide)
                        projectiles.remove(projectile)
                        compteur_asteroides = compteur_asteroides - 1
                        score= " :)"
                        score_text = font.render(f"Score: "+ score, True, (255, 255, 255))
                        msg = " a new player join the game"
                        cooldown_msg = 100
                        msg_text = font.render(f"" + msg, True, (255,255,255))
                        vaisseau_gost = pygame.image.load("vaisseauA.jpg").convert_alpha()
                        vaisseau_gost = pygame.transform.scale(vaisseau_gost, (80,80))
                        vaisseau2_gost = pygame.image.load("vaisseauA.jpg").convert_alpha()
                        vaisseau2_gost = pygame.transform.scale(vaisseau2_gost, (80, 80))
                        
                        
                        break
            
            
            
            
            
            
            # Mise à jour de la position de l'astéroïde (ajoutez votre logique de mouvement ici)
            angle_asteroide = math.radians(asteroide['direction'])
            asteroide['x'] += asteroide['speed'] * math.sin(angle_asteroide)
            asteroide['y'] += asteroide['speed'] * math.cos(angle_asteroide)

            # Gérer la sortie de l'astéroïde de l'écran
            if asteroide['x'] > 800 + asteroide['radius']:
                asteroide['x'] = 0 - asteroide['radius']
            elif asteroide['x'] < 0 - asteroide['radius']:
                asteroide['x'] = 800 + asteroide['radius']

            if asteroide['y'] > 600 + asteroide['radius']:
                asteroide['y'] = 0 - asteroide['radius']
            elif asteroide['y'] < 0 - asteroide['radius']:
                asteroide['y'] = 600 + asteroide['radius']
            
        if vaisseau_gost : 
            y_gost = y_gost - vitesse*math.cos(math.radians(angle_gost))
            x_gost = x_gost - vitesse*math.sin(math.radians(angle_gost))
            pivot_gost= (x_gost, y_gost)
        if x_gost > 800 + 25:
                x_gost = 0-25
                pivot_gost = (x_gost, y_gost)
            # Si le vaisseau dépasse le bord gauche, il réapparaît à droite
        elif x_gost < 0- 25:
                x_gost = 800 + 25
                pivot_gost = (x_gost, y_gost)

            # Si le vaisseau dépasse le bord bas, il réapparaît en haut
        if y_gost> 600+ 25:
                y_gost = 0-25
                pivot_gost = (x_gost, y_gost)
             # Si le vaisseau dépasse le bord haut, il réapparaît en bas
        elif y_gost < 0- 25:
                y_gost = 600+ 25
                pivot_gost = (x_gost, y_gost)
        
        luckturn = random.randint(0,1)
                    
        if luckturn == 0 and vaisseau_gost:
            angle_gost = angle_gost + 5 #avec 100 lui donne un air hors de controle 
            vaisseau2_gost = pygame.transform.rotate(vaisseau_gost, angle_gost)
            pivot_gost= (x_gost, y_gost)
        if luckturn == 1 and vaisseau_gost:
            angle_gost = angle_gost - 5
            vaisseau2_gost = pygame.transform.rotate(vaisseau_gost, angle_gost)
            pivot_gost= (x_gost, y_gost)

        # Dessiner et mettre à jour chaque projectile
        for projectile in projectiles:
            
            creation_de_projectile(projectile['x'], projectile['y'])
            

            

            # Mise à jour de la position du projectile
            projectile['x'] = projectile['x'] - math.sin(math.radians(projectile['angle'])) * projectileV
            projectile['y'] = projectile['y'] - math.cos(math.radians(projectile['angle'])) * projectileV

            # Gérer la sortie du projectile de l'écran
            if projectile['x'] > 800 + 5 or projectile['x'] < 0 - 5 or projectile['y'] > 600 + 5 or projectile['y'] < 0 - 5:
                projectiles.remove(projectile)
                if type(score)!= str:
                    score-= 50
                score_text = font.render(f"Score: {score}", True, (255, 255, 255))

            # Réduire le temps de vie du projectile
            projectile['lifetime'] -= 1

            # Supprimer le projectile s'il a épuisé son temps de vie
            if projectile['lifetime'] <= 0:
                projectiles.remove(projectile)
                if type(score) != str:
                    score -= 50
                score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        
        

        # Réduire le temps de recharge du projectile
        if projectile_cooldown > 0:
            projectile_cooldown -= 1
        if (compteur_asteroides) == 0:
            nombre_asteroides += 1
            compteurluck = 0
            asteroides = creation_asteroides(nombre_asteroides)
            compteur_asteroides = (3*nombre_asteroides) + compteurluck
            
        

        

        
        if Verif1 == True:
            acceuil("background2.jpg")

        # Dessiner les éléments de l'interface graphique (GUI)
        manager.update(time_delta / 1000)
        manager.draw_ui(screen)

        if vaisseau:
            rotated_rect = vaisseau2.get_rect(center=pivot)
            screen.blit(vaisseau2, rotated_rect.topleft)
        if vaisseau_gost:
            rotated_rect_gost = vaisseau2_gost.get_rect(center=pivot_gost)
            screen.blit(vaisseau2_gost, rotated_rect_gost.topleft)
        
        if score_text:
            screen.blit(score_text, (650, 10))
        if msg_text and  cooldown_msg > 0 :
            screen.blit(msg_text, (400, 300))
            cooldown_msg = cooldown_msg - 1

        
        
        if Verif3 == True:
            transition()
            Verif3 = False
        
        pygame.display.flip()
    
main()
