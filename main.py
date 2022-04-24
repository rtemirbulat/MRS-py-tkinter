import tkinter as tk
from tkinter import *
import os
from tkinter import filedialog
from ttkwidgets.autocomplete import AutocompleteCombobox

root = tk.Tk()
root.geometry("1350x540")
files = []
OPTIONS = [
    "Attorney Letter",
    "Funding",
    "Data Sheet",
    "Picture",
    "Certification of Driver License",
    "Affidavit of No Insurance",
    "EUO",
    "Bill Summary",
    "Police Report",
    "Patient Information",
    "Insurance card",
    "Insurance Information",
    "Cover Letter",
    "POM",
    "Consent to Change Attorney",
    "Law Agreement",
    "Medical records",
    "Law Verification",
    "Funding Agreement",
    "Intake Form",
    "NF-2",
    "Insurance Letter",
    "Email receipt",
    "Email from Attorney",
    "Email Confirmation",
    "Retainer Statement",
    "Liens",
    "Attorney Evaluation letter",
    "Attorney Agreement",
    "Notice of Denial",
    "NF-10","Peer Review","EOR", "Plaintiff's Response to Demands", "Plaintiff's Verified Answer", "Medical Reports and Doctor's lien",
]

data = [
    "Bonilla, Evaniel", "A Almontsir, Ibrahim", "A Caroll, Donre", "A Cruz, Isnacio", "A Delleguas, Luis",
    "A Encarnacion, Julio", "A Illustrious, Meyers", "A John, Samantha", "A Knox, Marlon", "A Mantack, Monique",
    "A Merricks, Michael", "A Mota, Carlos", "A Puello, Francisco", "A Rivera, Carlos", "A Romero, Claudia",
    "A Rosario, Michael", "A Vaughn, Maxine", "A Watts, Kristina", "A Wint, Sashire", "Abinader, Jose F",
    "Abraham, Abdias", "Abreu, Okalis Miguel", "Abreu, Ramona", "Abuzaid, Abdallah", "Acevedo, Maribel",
    "Acevedo, Maribel", "Acosta Almanzar, Alan", "Acosta, Candido", "Acosta, Junior", "Acosta, Kenny",
    "Acosta, Mariana", "Adams, Crystal", "Adrien, Rosalande", "Affinnih, Rabiat", "Afriyie, Juliessa",
    "Agbomah, Godwin A", "Aguilar-Chavez, Oscar", "Alarcon, Ana T", "Alawiye, Fati", "Albadawi, Ali",
    "Alcantara Macario, Jose Manuel", "Alcantara, Lourdes", "Alcantara, Victor", "Alcidas, Jean", "Alcivar, Pedro",
    "Alexandre, Jacques H", "Alexandre, James", "Alexis, Jerry", "Alfrena, Macklin", "Ali, Jabbar", "Alimatou, Jallow",
    "Alleyne, Maritza A", "Allonce, Steavens", "Allume Joseph, Marie Claude", "Almanzar, Chris", "Almanzar, Jennifer",
    "Almonte Batista, Eva M", "Almonte, Delvi", "Alonzo, Elizabeth", "Alphanso Stephenson, Michael",
    "Alsbrooks, Casey D", "Alston, Robert", "Alvarez, Jomary", "Alvarez, Jonathan B", "Alvarez, Teofilo",
    "Alvarez-Martinez, Rey Angel", "Alvin, Browne", "Amador Collado, Christhian", "Amador, Yendy A. Diaz",
    "Amador-Morales, Alvin", "Amaguay-Cantuna, Fanny", "Amaro Ramirez, Wander", "Amauri Castro, Albert", "Ancrum, Mica",
    "Anderson, Charles M", "Anderson, Jahmane Jamani", "Anderson, Nathan Uriah", "Anderson, Richard",
    "Andrews, Shaniqua", "Aneudy, Perez Blanco", "Angelica Suarez, Sharendalle", "Anthony Ancrum, Charles",
    "Anthony Machado, Richard", "Anthony, Mario", "Antigua Pacheco, Fredelin", "Antoine, Ernest", "Aponte, Elizeth",
    "Aquino De Tejada, Teresa", "Aracena, Felix A", "Arnette, Dyovahni", "Arredondo Duran, Elena", "Arroyo, Karen",
    "Arroyo, Sharon", "Arvelo, Valerie", "Asher, Yaakubov", "Atterberry, Tory P", "Auguste, Gregory",
    "Avalos Diaz, Alan", "Averhart, Maya", "Aybar, Dario", "B Camara, Fatoumata", "B Smith, Sherma", "Babaj, Ndreke",
    "Baez, Arleni", "Baez, Hipolito", "Bailon, Michelle", "Balashova, Elena", "Balbuena, Jonathan", "Baldwin, Kenya",
    "Baley, Nyshifah", "Baltazard, Frantzy", "Banegas, Bethy C", "Banks, Damien", "Banton, Kevoy", "Baptista, Joseph",
    "Barajas, Irma L", "Baretto Almodovar, Lizynel", "Barnes, Jermaine", "Barnes, Julius", "Barrett, Mark",
    "Bates, Sade", "Batichon, Sheedy Terry", "Batista, Angel", "Batista, Kenny", "Battle MacCormick, Shannon",
    "Battle, Anthony", "Bautista, Mircia R", "Bayevskiy, Daniel", "Bazile, Resia", "Beato, Michael",
    "Beaulieu Dorelus, Schebania", "Bell, Haakim", "Bellamy, Elena", "Bellamy, Nehemiah Andre", "Bellamy, Terence L",
    "Bellamy, Tyanna", "Bellamy, Tyanna", "Belotte, Shannen", "Beltre Ramirez, Luis M", "Benzant Carela, Luis Angel",
    "Bessard, Reuven", "Birch Jr, Tyrone", "Blackett Daly, Kerena Lisa", "Blackwood, Rashid", "Blaise, Pascal",
    "Blount, Antwon", "Bonilla, Matilde", "Botwe, George Kobina", "Boutin, Pierre", "Brady, Rosemarie E",
    "Brancoccio, James", "Brazoban De La Cruz, Miguel Alexander", "Brazoban, Fermin", "Brea, Pedro I",
    "Breville, Marvens", "Bristow, Mark Jr", "Brito, Enniris", "Brito, Omar J", "Brook, Keosha",
    "Brown Jr, John Joseph", "Brown Sr, John", "Brown, Aaliyah", "Brown, Abena", "Brown, David", "Brown, Fabian",
    "Brown, James", "Brown, Kisha", "Brown, Lyndira", "Brown, Omar", "Brown, Rodney", "Brown, Serezze",
    "Brown, Valerie C", "Bryan, Sharon", "Bryce Jr, Wayne A", "Budden, Immanuel", "Buenos Torres, Roberto De Jesus",
    "Burgos, Jessica", "Burgos, Karolyn M", "Burgos, Luis", "Burgos, Marlenny", "Burgos, Rafael", "Burton, Elijah",
    "Cabral, Leydania", "Cabreja, Eddie V", "Cabrera-Vasquez, Leonard R", "Caesar, Orin Joel", "Calixte, Jean Yonel",
    "Camacho, Bienvenido", "Camille, Jacques", "Camilo, Franchela M", "Campbell, Jamarr",
    "Campbell, Moriah Ivana Elisabeth", "Campbell, Nathaniel I", "Campos, Mercedes E", "Canario, Ronny",
    "Candelario, Glenys", "Canela, Sofia", "Cannon, Smith", "Caraballo, Jose", "Cardenas, Jocelyn",
    "Cardichon, Eian Michel", "Cardoza, Deyces Perez", "Carlos, Barahoma", "Carmona-Garcia, Irving Antonio",
    "Carobert, Patrick", "Carr, Corry", "Carrero-Ramos, Eva", "Carrion, Ivan", "Carter, Whitney J",
    "Carton Guzman, Maria", "Casado, Bryan", "Casimir, Cathia", "Castillo Henriquez, Charlies",
    "Castillo Rodriguez, Pedro", "Castillo, Dustin J", "Castillo, Leonardo", "Castillo, Omar", "Castro A, Freddy",
    "Castro, Jenalise", "Cayo, Daphne", "Celestin, Jean Michel", "Cepeda, Yorky", "Chalco Mejia, Genaro",
    "Chambers, Nicholas M", "Chan, Michael", "Chaplin, Saidah", "Chapman, Phillip", "Charles, Frantz",
    "Charles, Willem", "Cheatham, Tanisha", "Checo De La Hoz, Dariel M", "Checo De La Hoz, Mariel De Jesus",
    "Checo De La Hoz, Ramon Manuel", "Cherry, Roslyn", "Chery, Stephanie", "Chiza, Naiyhomi E", "Christophe, Yva",
    "Christopher, Davis", "Chrone, Patrick", "Cintron, Destiny", "Citron, Mark", "Clark, Brije", "Clark, Robert",
    "Clarke, Lajoy", "Clarke, Lauren", "Clarke, Stephen", "Cleveland, Roper", "Clezidor, Veronique", "Cliff, Candayce",
    "Coca Guzman, Francisco", "Cochrame, Tonya", "Colene, Alleyne", "Coley, Terrell", "Colimon, Holens",
    "Collado, Brunilda", "Collazo, Evesanly", "Collins, Almen", "Colon, Jamilka", "Colon, Julio", "Colon, Luis",
    "Comas, Gery", "Connor, Dencia", "Constant, Jeanwil", "Content, Lionel", "Contey, Gabriella", "Cooke, Jamesa",
    "Cooks, Ronald", "Cooper, Clarence", "Cooper, Shardei", "Cordero Nunez, Nelson A", "Cordero, Willie",
    "Cornick, Antoinette", "Corniel, Miguel", "Corniel, Rosse", "Coronado, Noemi", "Cosme, Krystal", "Craig, Franklin",
    "Crawford, Kayla", "Crews, Barbara", "Crews, Brianna", "Cruz Aquino, Grisel G", "Cruz, Beata", "Cruz, Christopher",
    "Cruz, Christopher", "Cruz, Erica", "Cruz, Grey", "Cruz, Grey", "Cruz, Jose F", "Cruz, Kevin", "Cruz, Lopez",
    "Cruz, Reneida R", "Cruz, Silo", "Cuesto, Marino", "Cuevas, Christopher", "Cumberbatch, Janiece J",
    "Curras, Jahaira", "Custodio Perez, Miguel E", "D Compere, Rose", "D Dorner, Diamond", "D Stanley, Raymond",
    "Dabouse, Celissaint", "Darwish, Zaher", "David Marin, Victor G", "David, Christopher", "David, Samuel",
    "Davis, Isabella", "Davis, Trevor", "Davis-Gaddy, Lillian", "De Jesus Cruz, Jose", "De Jesus, Maria",
    "De Jesus, Wilfredy", "De La Cruz, Luis Jose", "De La Rosa De La Rosa, Julio Cesar Manuel", "De La Rosa, Ivan",
    "De La Rosa, Joshua", "De La Rosa, Norberto", "De Leon, Maria", "De Leon, Richard", "De Los Santos, Alvaro",
    "De Los Santos, Franklin", "De Los Santos, Miladi", "De Paula, Gabriel", "Debrosse, Derrick", "Dejoie, Judith",
    "Dejoie, Krisna", "Del Orbe, Victor", "Dela Hoz, Ider Navas", "Delacruz, Carla", "Delaespada, Ronald",
    "Delarosa, Guadelupe", "Delgado, Roberto", "Dennison, Robert", "Denson, Yvette", "Deo Leo, Manuel",
    "Derival, Gladys", "Derival, Yvrose", "Desamours, Wisman", "Desravines, Jason", "Dessources, Kims",
    "Di Leone, Antonio", "Diaz, Angel Luis", "Diaz, Anthony", "Diaz, Cesar A", "Diaz, Hondina", "Diaz, Jose R",
    "Diaz, Robin Jr", "Diaz, Sasha", "Diaz, Yadira", "Dickson, Chrisstena", "Dieng, Abou S.", "Dieudonne, Guy R",
    "Dieujuste, Renaldo", "Diggins, Jordy", "Dionisio, Melo", "Dockery, Dwight", "Dodson, Crystal", "Dominguez, Andrew",
    "Dominguez, Ivelisse", "Dominique, Jasson J", "Dorissaint, Jean Richard", "Dornelus, Pierre J",
    "Dorneval, Kersainte", "Douze, Fedner", "Drake, Evaleen", "Duma, Jean", "Dunham, Rahiem", "Dupcil, Well Julson",
    "Dupre, Steven", "Duran Gonzalez, Martire", "Duran, Keyla", "Duran, Lino Arias", "Dutreuil, Donald", "Duval, Tony",
    "Duvel Germaine, Alexandre", "Duverge, Kirsy Waleska", "Dwhyte, Drysdale O", "Dyne, Jean", "E Molina, Valerin",
    "E Rivera, Carmen", "E Tolber, James", "Eagleston, Sophia", "Eberl Jolicoeur, Jean", "Edwards, Tunisa",
    "Elagmy, Adam H", "Elliott, Kelvin A", "Elliott, Rosemarie", "Encarnacion, Bryan", "Ephram, Terry",
    "Ermina, Joseph", "Espinal, Kenny", "Estevez Moreno, Scarlett", "Etienne, Stanley", "Evans, Chavanece",
    "Exilus, Jean", "Eze, Kevin", "F Bowers, Michael", "F Latacela, Kevin", "Fabien, Gardy", "Faeurazin, Evens",
    "Fana del Orbe, Johanna Ginette", "Fana, Angel T", "Fantauzzi, Wilmer", "Farmer, Destiny", "Farquharson, Rodrick",
    "Farrier, Tiffany", "Feiton, Akeem", "Felix, Chealove", "Feliz Ferreras, Sheila", "Feliz, Frandi E", "Feliz, Pedro",
    "Ferguson, Lamar", "Fernandes, Reshana", "Fernandez, Anastacia", "Fernandez, Francisco", "Fernandez, Francisco",
    "Fernandez, Joel", "Fernandez, Jose R", "Fernandez, Julio", "Fernandez, Raymundo", "Ferreras, Lidio",
    "Ferrer-Santos, Hector", "Fevry, Dudley", "Fevry, Marc", "Figaro, Claude", "Figueroa, Carlos", "Figueroa, Doris",
    "Figueroa, Reianna", "Filias, Jeannot", "Fils, Eden", "Firesteyn, Jonathan M", "Flaifel, Mohammad",
    "Flemmings, Wilton G", "Florencio-Gomez, Maria P", "Flores, Daniel J", "Flores, Fidel", "Floyd, Raheem",
    "Folks, Carlene C", "Folks, Willoughby III", "Follett, Sylvan", "Fontanez, Christina", "Ford, William",
    "Forderingham Sanchez, Jennea", "Fortune, Berley", "Fosphero, Atlas", "Foster, Kennardo", "Fraizer, Bassell",
    "Francis, Chantal", "Francis, Dean A", "Francis, Gabbi", "Francois, Junior", "Francois, Mario",
    "Frazier Jr, Edmond", "Frazier, Martin", "Freeman, Duantae", "Freeman, Loretta", "Frias, Genesis", "Fuentes, Joel",
    "G Blaise, Aldho", "G Matthew, Karissa", "Gabbidon, Roy Antonio Jr", "Gabriel, Jean", "Gaines, Donald",
    "Galan-Castillo, Maximo", "Galichenko, Viacheslav", "Galva Gutierrez, Vianny", "Gambrell, Brenden",
    "Gamez Duarte, David", "Garay-Torres, Deborah", "Garcia de Figaris, Grey", "Garcia Duran, Felipe",
    "Garcia Santos, Cristian", "Garcia, Angery", "Garcia, Carlos", "Garcia, Delfin I", "Garcia, Diego A",
    "Garcia, Ivelisse", "Garcia, Juan", "Garcia, Omar", "Gary, Latisha", "Gedeon, Ketiana", "Genao Pereya, Julissa",
    "Genao, David", "Genao, Yanibel", "Genoveffa, Mazzella", "Gentry, Kemesha L", "German, Dionis A. Pena",
    "German, Zeneida", "Geston, Lycess", "Gevens, Joseph", "Gilbert, Nigel", "Gilchrist, Marvin", "Gilles, Garry",
    "Gilles, Marguerite", "Gilmore, Shanayia M", "Gilyard, Christopher", "Gilyard, Christopher", "Glen, Donnette",
    "Glenn, Kelsey", "Gollardo, Marvin", "Gomez, Herbet", "Gomez, Wilson R", "Gomez, Yenelda",
    "Gomez-Lizardo, Vimeslyn V", "Gonzalez Beato, Six Clary Mercedes", "Gonzalez Garcia, Carlos", "Gonzalez, Cleritza",
    "Gonzalez, Doris", "Gonzalez, Elias", "Gonzalez, Erikka", "Gonzalez, Erikka", "Gonzalez, Jeffry",
    "Gonzalez, Roger Adan", "Gonzalez, Ruben", "Gonzalez, Ruth", "Gonzalez, Shelsy", "Gonzalez, Steven",
    "Gonzalez, Yaileny", "Gordon, Althea", "Gordon, Jevon", "Gordon, Wilfredo", "Goude, Robert", "Goytia, Crispin N",
    "Grant, Tyreek", "Gray, Nicole", "Green, Shalena", "Green, William", "Greenberg, Anna", "Grell, Raymond",
    "Griffin, Tyree", "Griffith, Erica", "Griffiths, Mikhail", "Grisset, Shaquan", "Guerin, Volvedge",
    "Guerrero Monegro, Pedro", "Guerrero, Denzel", "Guerrero, Jayden", "Guerrero, Pedro F", "Guerrier-Mars, Naomie",
    "Guervil, Guima", "Guidote, Jasmin", "Guillaume, Steve", "Guinn, Robert L", "Guirand, Deromme",
    "Guiti Bonilla, Jeison", "Gutierrez de Jimenez, Candida A", "Guy, Allain", "Guzman Tejada, Wilben",
    "Guzman, Domingo A", "Guzman, Urcania Alvarado", "H. Diallo, Ahmadou", "Hall, Sia A", "Hall, Sia A",
    "Hamilton, Duce", "Haney, Latisha", "Hanns, Quishaun", "Harding, Winston", "Harris, Ngina", "Harry, Francis",
    "Harze, Rashawn", "Hasitha, Henegama", "Hendricks, Claudette", "Hendricks, Shanice", "Henriquez, Cinthia",
    "Henriquez, Eddymell", "Hensford, Marlon", "Herard, Sayonara", "Hernandez Perez, Erickson",
    "Hernandez Perez, Katherine", "Hernandez, Alexsa", "Hernandez, Aneudy", "Hernandez, Angel R",
    "Hernandez, Brianie A", "Hernandez, Dionisia", "Hernandez, Jean Carlos", "Hernandez, Jessenia",
    "Hernandez, Jessica", "Hernandez, Luilly J Cabrera", "Hernandez, Luis", "Hernandez, Patricia", "Hernandez, Sulay R",
    "Hernandez, Yahaira", "Hernandez, Yessy", "Herod Young, Asheley K", "Herrera Dorminguez, Mauro", "Heynes, Vernal",
    "Hidalgo, Brownie Lopez", "Hidalgo, Chrisanthony", "Hilaire, Widlie", "Hill, Jeffrey", "Hinds, Orundell",
    "Hobal, Chris", "Hodges, Emanuel", "Holder, Terall S", "Holness, Breanna", "Holness, Flora", "Hooper, Courtney",
    "Hosein, Jennah S", "Howard Jr, Montreal", "Howard, Andrea", "Howard, James", "Hudson, Takira", "Hughes, Richard",
    "Hulen, Marlon", "Hyppolite, Jean", "Idelfonso, Rafael", "Igbinosun, Irobun E", "Infante Almonte, Erickson A",
    "Ingreed Lamour, Audrey", "Islam, Haimoon", "Iwuagwu, Chineye", "J Codio, Esther", "J Gittens, Terrence",
    "J Lewis, Kyle", "J Tavares, Baury", "J Walton, Davon", "Jackson, Yvette", "Jacob, Marjorie", "Jacobs, Deaisia",
    "Jacobs, Teraza D", "Jacques, Esther", "Jacques, Ruben", "James, Harley", "James, Kelly", "Jarrett, Kemar J",
    "Jasharevic, Keriman", "Jashari, Floriant", "Jean Baptiste, Kingsley", "Jean Charles, Zavier",
    "Jean Claude, Kesler", "Jean Gerald, Leandre", "Jean Gilles, Junior", "Jean Pierre, Gueldie", "Jean, Gregory",
    "Jean, Jonas", "Jeffrey, Martinez", "Jemmott, Anthony", "Jermain, Roberto", "Jermaine, Spencer", "Jeter, Jawann",
    "Jett, Keniesha Moncel", "Jimenez, Alberth", "Jimenez, Anthony", "Jimenez, Bienvenido", "Jimenez, Jhon",
    "Jimenez, Joel R", "John Michael, Stanastley", "John, Kitt", "Johnson, Antonio", "Johnson, Brian",
    "Johnson, Chris L", "Johnson, Earline", "Johnson, Hugo", "Johnson, Tihirah", "Jones, Clemento", "Jones, Donavon",
    "Jones, Latrica", "Jones, Mwanze", "Jones, Rasuan B", "Jones, Tareke", "Jorge, Alexander", "Jorge, Jairo A",
    "Jose Cruz, Juan", "Jose Mejillones, Juan", "Jose Reyes, Juan", "Jose, Liriano Cruz", "Joseph, Asia",
    "Joseph, Chantal", "Joseph, Cheryl M", "Joseph, Jean R", "Joseph, Kazan T", "Joseph, Stanley", "Joseph, Sunina",
    "Joseph, Wadson", "Jouravlev, Mikhail", "Julien, Wendy", "Junior Clairville, Francis", "K Dore, Mohamed",
    "Ka Seidu, Patrick", "Kanmou, Etienne", "Karsos, John", "Kelly, Rodney", "Kelly, Shron", "Khem, Linda",
    "Khusainov, Damir", "Khusainova, Gulfiya", "King, Cecil R", "Kingston, Jinelle", "Kirama, Jamal", "Kirama, Rajaa",
    "Kirkland, Jerry", "Knight, Davon", "Kollock, Shaina L", "Korchak, Yuliya", "Koshkin, Michael", "Koshkin, Russell",
    "Krystal Wade, Alicia", "L Diaz, Jose", "L Jorge, Jose", "L Matta, Christopher", "L Polanco, Daniel",
    "L Rodriguez, Anthony", "L Tucker, Michael", "Labaze, Nicdarley", "Laboy, Rolando", "Ladouceur, Adolphe",
    "Lafleur, Herve", "Laguda, Olabayo", "Laguerre, Aryelle C", "Lake, Jahkin", "Lall, Fiona", "Lall, Rohan",
    "Lall, Thara", "Lantigua Tejada, Esteban", "Lantigua, Christopher", "Larios, Elias", "Lark, Courtney",
    "Latoya Tornlinson, Anna-Kay", "Laurore, Herlide", "Lawrence, Ciara", "Lawrence, Keishana", "Lawrence, Tarel",
    "Lawson, Latisha", "Leak, Theodore", "Lebrun, Jacques", "Lee Estevez, Bryant", "Lee, Charles", "Lee, John",
    "Lefranc, Kiya", "Lefroy, Patrick", "Lemite, Yann", "Lentz, Phillip", "Leoin, Matthew",
    "Leonardo Marte, Michael De Jesus", "Leslie, Omari O", "Lessey, Kalilah", "Lester, Taylor", "Level, Alexis",
    "Lewis, Vickie", "Lilly, Brenda", "Lilly, Charice S", "Lin, Peidong", "Lindo, Hector R", "Lino, Jairo",
    "Linwood Carter, Craig", "Liranzo, Dorca", "Liriano Cruz, Carlos", "Littlie, Shawn", "Livingston, Richard",
    "Lizardi, Edwardo", "Lizardo-Sanchez, Amelci A", "Loginskii, Sergei", "Lopez Mendez, Sabiel Andres",
    "Lopez Mendez, Sabiel Andres", "Lopez, Daniela", "Lopez, Javier", "Lopez, Juan", "Lopez, Marcos M", "Lopez, Miguel",
    "Lopez, Nayelis", "Lopez, Ricardo", "Lopez, Sacha A", "Lopez, Sadir", "Lormeus, Francesca", "Lott, Ricky B",
    "Louima, Marie", "Louis, Harry Pierre", "Louis, Jean", "Louis, Jean-Pierre", "Louisma, Christian",
    "Lovelace, Thomas", "Lozano Mundaray, Paola", "Lucas, Jemari", "Lugo Luna, Johanna", "Lugo, Lucero Fernandez",
    "Luis Coache, Jose", "Luna Martinez, Joselyn A", "Luna Montes, Lazaro", "Luna, Octavia", "Luzon, Dimas",
    "Lyubimtseva, Sofia", "M Bowers, Robert", "M Delince, Jeremiah", "M Jean-Henry, Valerie", "M Lawrence, Kim",
    "M Oleaga, Ronny", "M Sandoval, Jamel", "M Weeks, Stephen", "MacCormick, Morgan", "Maccow Neddall, Oscar G",
    "Mahmoud, Mohammad", "Majin Males, Ruben D", "Maldonado de Polanco, Sonia D", "Maldonado, Juan", "Malick, Gai",
    "Mallari, Hector J", "Mann, Leon", "Mann, Uriah", "Mansouri, Wafaa", "Manuel Sanabria, Victor", "Manvelidze, Shota",
    "Marc, Jaques", "Marcelin, Michaud", "Marcelin, Nunecar", "Marcellus, David", "Marcelus, Marvin",
    "Marie Singh, Evelyne", "Marie, Eloi", "Marius, Donovan", "Marmar, Igal", "Marseille, Beckerson",
    "Marseille, Kerline", "Marshall, Jacqueline", "Marte Murga, Taharie Marie", "Martin, Dennis K", "Martin, Renair",
    "Martinez Alcantara, Javier Oli", "Martinez Martinez, Alejandro", "Martinez Melendez, Jhonatan",
    "Martinez, Cherise", "Martinez, Erica", "Martinez, Evangelique", "Martinez, Gaudy", "Martinez, Jessie",
    "Martinez, Jesus", "Martinez, Jose", "Martinez, Jose Daniel Calvio", "Martinez, Melquisedec", "Martinez, Shamieka",
    "Mateo Blanchard, Evelyn T", "Mateo, Desteny", "Matos Mass, Antoannette", "Matthew, Trevor", "Matthew, Vixama",
    "Maura, Elibardo", "Maurice, Geordany", "Maurice, James", "Mazie, Kajja C", "Mazil, Leroy", "McCallum, Jahtique",
    "McCowen, Constance", "McCowen, Constance N", "McCrea, Kareem A", "Mccurchin, Christopher", "McDaniel, Tiffany",
    "McDonald, Iesyia", "McDowell, Damonte G", "Mcghee, Keith", "Mckenzie, Nyasha", "McLean, Brian", "Mede, Rousso",
    "Medina, David", "Mejia, Cecil R Jr", "Mejia, Fausto", "Mejia, Johanny", "Mekhanik, Natalya",
    "Melendez, Cameron Calderon", "Mella, Rikelby", "Mella, Tatianna", "Melvin, Jack", "Mena, Jose", "Mency, Eric",
    "Mendez, Shamal", "Mendez, Yobari", "Menzies, James", "Meran Infante, Cristian M", "Mercado, Hector",
    "Mercado, Liany", "Mercer, India", "Merisiers, Djeniva Sarah", "Mesa, Nicole", "Michael, Reinoso",
    "Michelle, Descardes", "Milagros, Acevedo", "Miles, Brandon A", "Milete, Zuleimy", "Milevoix, Alex",
    "Minderson, Andre", "Minosyan, Makhitar", "Minouche, Ciceron", "Mirabel, Jonathan", "Mitchell, Melissa",
    "Mitchell, Peecoa", "Modestil, Daive", "Moise, Jean", "Mondelus, Ernst", "Monroy, Melinda M", "Montanez Jr, John",
    "Montolio, Moriel", "Moore, Wendell", "Mootoo, Elisandra E", "Mora Diaz, Rosa E", "Morales Vidal, Jose L",
    "Morales, Maria V", "Morales, Rigoberto", "Morales, Wyllie", "Moran, Charlene", "Moran, Jovanna",
    "Moranchel, Maria Flores", "Morel, Albert", "Morera, Raul", "Morgan, Dalton", "Morillo Beriguete, Mariano",
    "Moris, Daisy L", "Moris, Lucinda", "Morris, Unique", "Morrison, Omar", "Morrison, Samantha", "Moskowitz, Renee",
    "Moye, Charles", "Moze, Ashmir", "Muhammad, Yadullah", "Murad, Gibbs", "Muratori, Andrea", "Musleh, Abdulhamid",
    "N Pierre, Jean", "Naoum, George", "Narea, Laura", "Natera, Isis N", "Nazario, Edwin", "Nazario, Monique",
    "Ngo Bakouble, Catherine", "Nibbs, Jermaine", "Nibbs, Jermaine", "Nicasio De Arias, Karina", "Nicolas, Lionel",
    "Nicolas, Marie", "Nieves Velez, Reynaldo", "Nieves, Alfredo", "Nimotalahi, Badmus", "Noel, Wade", "Noesi, Yumilsa",
    "Nolasco, Esmeralda", "Nunez Benitez, Melanny", "Nunez, Anthony Jose", "Nunez, Melanny", "Nunez, Melanny",
    "O Taveras, Julissa", "Obando, Raven M", "Oladipo, Ajibola", "Olga Davius, Catherina", "Oliver Nichols, Anthony",
    "Oliveri, William", "Omar Rodriguez, Luis", "Orangene, Romero", "Orelano-Villafan, Kelly", "Ortiz Jr, Nelson",
    "Ortiz, Crist J", "Ortiz, Deisy G", "Ortiz, Evelyn", "Ortiz, Irma", "Ortiz, Kristian", "Ortiz, Malaysha",
    "Ortiz, Patricia", "Orville Spencer, Shawn Jr", "Osorio, Glenda", "Otanez, Lourdes", "Otero, Carlos",
    "Ouedraogo, Abdoul", "Ovalles, Sol", "Ovando, Andreina", "P Cando, Olga", "P Larose, Anastasha", "P Ruiz, Joshua",
    "Pablo Guzman, Juan", "Pacheco, Carmen", "Pacheco, Jayson", "Padilla, Rubinsky", "Paez, Raidy", "Palmer, Otis",
    "Pantaleon, Maria", "Pantoja, Angela", "Parker, Anthony L", "Parks, Michael A", "Pasternak, Yuriy",
    "Patino, Dominick", "Patlakh, Aleksander", "Patlakh, Maryana", "Patterson, Emanuel", "Paul Piedra, Marco",
    "Paul, Dencel", "Paul, Eric", "Paulino Camilo, Yasmin", "Paulino Jimenez, Melvin", "Paulino Jimenez, Melvin",
    "Paulino Nunez, Eddy", "Peguero Sanchez, Julissa A", "Pena de Rodriguez, Franciny M",
    "Pena Ogando, Wilvany Alexander", "Pena, Maria E", "Pender, Sheryl", "Penn, Lavern", "Peralta Rijols, Fausto A",
    "Peralta, Claudia", "Peralta, Minorka", "Perdikakis, Heaven N", "Perez Lopez, Jesus", "Perez Nunez, Franklyn L",
    "Perez Quiroga, Cesar A", "Perez Valoy, Delio", "Perez, Carolina", "Perez, Elizabeth", "Perez, Keyanna",
    "Perez, Nadia N", "Perez, Rena", "Perez, Sagrario", "Perez-Reyes, Joelly M", "Perking, Jahjuan",
    "Perrault, Brandon", "Perrineau, Shakira", "Persaud, Kumar", "Persaud, Salita", "Peterson, Ceraphin",
    "Philemon, Duvalson", "Phillip, Renee S", "Phillips, Theador", "Pierre Paul, Rodalbert", "Pierre, Anderson",
    "Pierre, Carmelle", "Pierre, Murat", "Pierre, Obespierre", "Piervil, Franck R", "Pignard, Miche", "Pimentel, Ambar",
    "Pimentel, Glendys", "Pizarro, Anthony", "Placido Reynoso, Marcelino", "Pogue Jr, Eric", "Polanco Acosta, Maria C",
    "Polanco, Jose D", "Polanco, Juan J", "Polanco, Rosa", "Polidura, Joanna", "Polo, Maximilyan M", "Post, Crystal",
    "Powell, Brian", "Pratt, Tyliek", "Precil, Marie", "Preval, Jennifer", "Previlon, Jessica", "Prieto, Kysis C",
    "Q K Herbert, Emile Junior", "Quamina, Ronda M", "Quattlebaum, Kareem", "Quezada, Jazmin", "R Vasquez, Mark",
    "R Webb Jr, Clarence", "Ramales, Maricela", "Ramirez De Urraca, Sujeidy", "Ramirez Gil, Junior",
    "Ramirez, Alejandrin M", "Ramljak, Stefan", "Ramon, Ariza", "Ramos, Bienvenido E", "Ramos, Emily",
    "Ramsey, Shaahidah", "Raposo, Naomy", "Reid, Jermaine", "Remy, Dadia", "Rene, Djoory", "Rene, Jean",
    "Rene, Jean Gerard", "Rene, Jean R", "Rene, Nelf T", "Rennie, Jamal", "Retama, Manuel", "Reyes, Anthony",
    "Reyes, Desiree Krystal", "Reyes, Victor Amaury", "Reynoso, Jose", "Reynoso, Julian", "Reynoso, Odalis",
    "Reynoso, Yuberky", "Rhames, Valerie", "Rhejime, Henry R", "Rhobe, Seon", "Ribenson, Eliezer", "Richards, Andrea",
    "Richardson, Monique", "Richardson, Zipporah", "Riddick, Infiniti", "Rincon Ramirez, Cesarin",
    "Rios-Cabot, Gabriel", "Rivas, Henry", "Rivera, Albin", "Rivera, Jacqueline", "Rivera, Joselyn", "Rivera, Kevin",
    "Rivera, Luis", "Roa, Amaya", "Roacher, Michael M", "Roberson, Carelus", "Robinson, Clinton", "Robinson, Ernest M",
    "Robinson, Kimberly", "Robinson, Milagros", "Rodriguez, Alejandro", "Rodriguez, Carlos M", "Rodriguez, Francisco",
    "Rodriguez, Jose R", "Rodriguez, Josue", "Rodriguez, Juan", "Rodriguez, Krystle", "Rodriguez, Luis",
    "Rodriguez, Ramon", "Rodriguez, Ricardo", "Rodriguez, Ricardo", "Rodriguez, Shana", "Rodriguez, Solanlli",
    "Rodriguez, Vanessa", "Rodriguez, Yanetsi", "Rodriques, Patrick", "Rofrano, Brandon", "Rofrano, Matthew",
    "Rogiers, Roxie", "Rogiers, Roxie", "Rojas Yumbla, Cinthya", "Romain, Robert", "Roman, Vanessa", "Roman, Wanda",
    "Romero-Castillo, Bienvenido", "Romulus, Manoucheka", "Ronaldo Reyes, Brandon", "Ronny, Jean",
    "Rosa Hernandez, Brailin J", "Rosa, Raymond", "Rosa, Yolanda", "Rosado, Dawnyn", "Rosado, Ernesto J",
    "Rosado, John E", "Rosado, Pablo", "Rosano, Israel", "Rosario, Carlos J", "Rosario, Enrique", "Rosario, Jessica J",
    "Rosario, Lisa", "Roseny, Buly", "Ross, Clarance", "Royal, Lij", "Ruiz, Obed", "S Davis, Makeda",
    "S Morrison, Janiqua", "S Ross, Shaihaba", "S Villagomez, Rafael", "Sabin, Amanda", "Sadok, Leshye",
    "Sadok, Leshye", "Saho, Ismaila", "Saidov, Rustam", "Saint Leger, Chris", "Saint Preux, Samy",
    "Saker Djoumbi, Kelly", "Salazar, Anibal", "Saldano, Jose", "Saleh, Abdulsalam", "Salem, Khalid",
    "Salgado, Roman Diaz", "Salomon-Garcia, Jorge", "Salvatore, Sedita", "Samuel, Claudette H", "Samuels, Daymon",
    "Sanchez Melendez, Alfonso", "Sanchez, Aracelis", "Sanchez, Chaxanne", "Sanchez, Crystal", "Sanchez, Hector",
    "Sanchez, Iris", "Sanchez, Leandro", "Sanchez, Lucas L", "Sanchez, Maria T", "Sanchez, Martha", "Sanchez, Michael",
    "Sanders, Deondre", "Sandoval, Milady", "Sanon, Beatrice", "Santa, Nancy", "Santana, Angelique",
    "Santana, Fraicer C", "Santana, Tiffany", "Santiago, Carmen", "Santiago, Esualdo J", "Santiago, Jasmin",
    "Santiago, Jose", "Santiago, Neraida", "Santora, Patricia", "Santos Guzman, Roberto", "Santos, Felix R",
    "Santos, Francisco", "Santos, Juan T", "Satnarine, Kayla", "Schnaider, Erika", "Scott, Seneesha", "Seda, Samantha",
    "Segura, Xiomara J", "Sepulveda, Melvin", "Seraphin, Chenet", "Sergeyeva, Lyudmila", "Serra, Vianel",
    "Serrano, Victoriano", "Shawn, Christopher", "Shell, Neffertitti", "Sheperd, Eugene", "Shepherd, Rebecca",
    "Shkundin, Allan", "Shuler, Tracy", "Shultz, Roger", "Silva, Jennifer", "Simms, Adrian", "Simon, Alicia",
    "Simon, Lamour", "Simpson, Divia", "Singh, Bidar", "Singh, Joginder", "Singletary, Naim", "Singleton, Geraldine",
    "Singleton, Rita", "Singleton, Shawnese", "Skeete, Esan", "Sky, Nataly", "Slade, John", "Smart, Latifah",
    "Smiley, Courtney U", "Smith Davis, Omar", "Smith, Anthony", "Smith, Deanna", "Smith, Eugene", "Smith, Garvin L",
    "Smith, Kenneail", "Smith, Nicole", "Smith, Ronald", "Smurden, Jacob", "Solis, Jefferson", "Sonese Colonel, Marie",
    "Sonia, Cean Marie", "Soriano, Rocio", "Sosa Mundaray, Mikaury", "Sosa, Alondra", "Sosa, Claudio", "Sosa, Franklin",
    "Soto, Sol", "Souffrant, Pierre", "Spady, Leon", "Spencer, Milaidi", "Spigner, Richard L", "St. Cyr, Thamar",
    "Starke, Hilliard", "Starks, Kareem", "Starlin Sanchez, Fabian", "Stephane Anglade, Joel",
    "Stephen Robinson, Carlton St", "Sterling, Devidette N", "Stewart, Johnny", "Stitch, Reginald", "Striplin, Aethena",
    "Stroman, Darrien", "Suares, Denzel", "Suarez De Santana, Angela M", "Suarez, Argentina", "Suarez, Edgardo",
    "Suero Gonzalez, Roberto", "Surgho, Jean L", "Sylla, Joseph", "Sylva, Mozoul", "Sylvestre, Ann",
    "Sylvestre, Galine", "Sylvestre, Jennifer", "T Moreno, Natasha", "T Okobi Jr, Obidinna", "T Shand, Mylicia",
    "T Wilson, Demond", "Talyzin, Mikle", "Tamas-Delgado, Christopher", "Tavarez, Yostyn", "Tavazz, Priscilla M",
    "Taylor, Iva", "Taylor, Vincent P", "Tayquan Morris, Unique", "Tejada Garcia, Comeiny", "Tejada Lee, Raysa",
    "Tejada, Krystle", "Tejada, William Tejada", "Tena, Jose", "Terrero, Claritza", "Thankgod, Amedu",
    "Thomas, Jermaine", "Thomas, Lyndon", "Thomas, Tiffany", "Thompson, Bernard", "Thompson, Deloid O",
    "Thompson, Joseph", "Thornton, Zenia", "Tifre-Norales, Luis", "Tihomirova, Inna", "Tirado, Nancy",
    "Tiru Ramos, Xavier", "Tonye, Martin", "Torres Gil, Christopher", "Torres, Candy", "Torres, Carmen",
    "Torres, Earline L", "Torres, Eva Maria", "Toumba Creole, Aurelie Ndengue", "Towles, Isaiah", "Townsend, Shirley",
    "Traore, Mamadou", "Trivino, Fernando", "Trometa, Branigan", "Udechi, Michael", "Urena Reyes, Jonel B",
    "Urena, Josias", "Urena, Keury", "Urena, Narely M", "Urena, Robinson L", "Urena, Samuel", "Ureta, Rebecca",
    "Urquhart, Basil", "V Morel, Michell", "Valdes, Shareal", "Valdez Mercedes, Luis", "Valerio, Carla",
    "Valladares, Alexander L", "Valle Cabanas, Yeni", "Vallejo Batista, Alejandro", "Vallejo, Juan B",
    "Valoy, Raelvy E", "VanHolt, Tachinque N", "Varela, Angel L", "Varela, Samantha L", "Vargas Diaz, Jose",
    "Vargas, Andy", "Varona, Rodney", "Vasquez, Ariel", "Vasquez, Carlos J", "Vasquez, Jamie", "Vasquez, Justin",
    "Vasquez, Pablo", "Vasquez-Ceballas, Jarol", "Vazquez, Gianna", "Veizman, Abraham", "Velez, Jose", "Veloz, Joel",
    "Ventura, Ramon", "Verlus, Hennesy", "Vernon, Simone", "Vertus, Jean-Louidor", "Vertus, Jean-Louidor",
    "Vesprey, Andrew B", "Victor, Trevor", "Vidal, Leonishia", "Vieux, Francesca", "Villafane, Nancy",
    "Villagomez, Gladys", "Vilmond, Marie ange", "Vincent, Guerson", "Vinson, Basheer", "Vital, Kindzor",
    "Vulfson, Svetlana", "Waddell, Phyllis", "Walden, Treazure", "Wallace, Winston", "Walters, David", "Warren, Latima",
    "Warren, Stewart", "Washington, Collynn", "Waters, Anthony", "Watson, Bernard", "Watson, Karizma",
    "Wedderburn, Shawn", "Weller, Patrick A", "Wellington, Tejeda", "Wendly Jean, Prophete", "Wertz, Joshua",
    "West, Rochelle M", "West-Henry, Jacqueline A", "Weston, Quajion", "White, Alaja", "White, Emanuel J",
    "White, Michael", "Wilamena, Jn Baptiste", "Williams, Amanda", "Williams, Christinea", "Williams, Corey",
    "Williams, Emir Cunningham", "Williams, Kimisha", "Williams, Louis", "Williams, Michael A", "Williams, Patricia",
    "Williams, Peter", "Williams, Tamara N", "Williams, Taneha", "Williams, Tyricka", "Williams, Wayne",
    "Williamson, David", "Willis, Zelia", "Wilson, Charles", "Wood, Ventera", "Wood, Ventera", "Wright, Nurlin",
    "Wright, Tyleyah", "Wunderlich, Philip", "Wynter, Lennox", "Ynoa, Rafael A", "Yusufova, Zemfira", "Yves, Fanfan",
    "Zacarias, Maria A", "Zachary, Ashlee Jahneece", "Zachary, Ashlee Jahneece", "Zapatalora, Rosaria N",
    "Zarzuela De Rodriguez, Sandra", "Zelada, Michelle", "Zelenaya, Bella", "Zinzi, Chalon"
]

#fax variable
fax= IntVar()
# fills listbox with files in curr dir
def OpenDir():
    listbox.delete(0, END)
    current_directory = filedialog.askdirectory()
    for file in os.listdir(current_directory):
        listbox.insert(END, file)
    folder_lb.config(text=os.path.abspath(current_directory))

#function to display current file
def selected_item(event):
    widget = event.widget
    selection = widget.curselection()
    picked = widget.get(selection[0])
    label.config(text=picked)
#opens popup when file already moved
def open_popup():
    top = Toplevel(root)
    top.geometry("120x70")
    top.title("FileNotFoundError")
    Label(top, text="File already removed & moved or does not exist!").place(x=0, y=0)
#main renaming function
def RenameFile():
    file_to_rename = label['text']
    working_dir = folder_lb['text']
    custom = inputtxt.get("1.0", "end")
    type = entry4.get()
    if fax.get():
        new_name = entry1.get() + " " + entry2.get() + " " + entry3.get() + " " + custom.strip() + " " + type +" FAX "
    else:
        new_name = entry1.get() + " " + entry2.get() + " " + entry3.get() + " " + custom.strip() + " " + type
    try:
        os.rename(working_dir + "/" + file_to_rename, working_dir + "/" + new_name + ".pdf")
    except FileExistsError:
        index = ''
        while True:
            try:
                os.rename(working_dir + "/" + file_to_rename,working_dir+"/"+ new_name+index+".pdf")
                break
            except WindowsError:
                if index:
                    index = '(' + str(int(index[1:-1]) + 1) + ')'  # Append 1 to number in brackets
                else:
                    index = '(1)'
                pass

    except FileNotFoundError:
        open_popup()
#clear selections
def Clear():
    inputtxt.delete('1.0', END)
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)#choose option reset
    label.config(text="")

# frame for selection and selection label with scrollbar
listbox = Listbox(root, width=40, height=300, selectmode="SINGLE")
listbox.pack(side=LEFT, padx=30, pady=30, fill=NONE)
scrollbar = Scrollbar(root)
scrollbar.pack(side=LEFT, fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
frame = tk.Frame(root, padx=10, pady=20, bg="white")
frame.pack(anchor="n", after=listbox, side=TOP)
# Label of listbox
files_label = tk.Label(root, text="Files: ", bg="white").pack(anchor=NW, padx=30, ipadx=20, ipady=2, before=listbox)

# label of selection
fr = tk.Frame(root, borderwidth=1, bg="white")
fr.pack(anchor="nw")
selected = tk.Label(fr, bg="white", text="Выбранный файл:")
selected.pack(anchor="nw", side=LEFT)
label = tk.Label(fr, bg="#dbdbdb", width=40)  # displays selected file
label.pack(anchor="nw", padx=10, pady=10, side=LEFT)

# label of folder
folder = tk.Label(fr, bg="white", text="Папка:")
folder.pack(anchor="nw", side=LEFT)
folder_lb = tk.Label(fr, bg="#dbdbdb", width=50)
folder_lb.pack(anchor="nw", padx=10, pady=10, side=LEFT)

# renameto
rename = tk.Label(root, text="Переименовать на:")
rename.pack(anchor="nw", side=TOP, padx=5, pady=5)

# frame with selection
fr2 = tk.Frame(root, borderwidth=2, bg="white")
fr2.pack(anchor="nw", after=rename)
patients = tk.Label(fr2, bg="white", text="Клиенты :")
patients.pack(anchor="nw", side=LEFT)
entry1 = AutocompleteCombobox(fr2, width=30, completevalues=data)
entry1.pack(side=LEFT, padx=10, pady=10, anchor="nw")
entry2 = AutocompleteCombobox(fr2, width=30, completevalues=data)
entry2.pack(side=LEFT, padx=10, pady=10, anchor="nw")
entry3 = AutocompleteCombobox(fr2, width=30, completevalues=data)
entry3.pack(side=LEFT, padx=10, pady=10, anchor="nw")
fax_c = Checkbutton(fr2,text="FAX?",variable=fax,onvalue=1,offvalue=0)
fax_c.pack(side=LEFT, padx=10, pady=10, anchor="nw")


# frame of custom input
fr3 = tk.Frame(root, borderwidth=2, bg="white")
fr3.pack(anchor="nw", after=fr2, pady=10)
# custom_input
custom_input = tk.Label(fr3, bg="white", text="Свободный ввод :")
custom_input.pack(anchor="nw", side=LEFT)
inputtxt = tk.Text(fr3, height=1, width=40)
inputtxt.pack(side=LEFT, padx=10, pady=10, anchor="nw")

# frame type of file
fr4 = tk.Frame(root, borderwidth=2, bg="white")
fr4.pack(pady=10, padx=5, side=RIGHT, after=fr2, anchor="n")
type_input = tk.Label(fr4, bg="white", text="Тип документа :")
type_input.pack(anchor="nw", side=LEFT)
#dropdown = OptionMenu(fr4, appendix, *OPTIONS)
#dropdown.config(width=10)
#dropdown.pack(side=LEFT, padx=10, pady=10, anchor="nw")
entry4 = AutocompleteCombobox(fr4, width=50, completevalues=OPTIONS)
entry4.pack(side=LEFT, padx=10, pady=10, anchor="nw")


# buttons

rename = tk.Button(root, text='Переименовать', padx=10, pady=20, command=RenameFile, width=10, bg='brown', fg='white')
rename.pack(side=RIGHT, padx=10, pady=10, after=fr, anchor="n")

clear = tk.Button(root, text='Очистить', padx=10, pady=20, command=Clear, width=10, bg='brown', fg='white')
clear.pack(side=LEFT, padx=5, pady=10, anchor="nw")

openFile = tk.Button(root, text="Open Folder", padx=10, pady=20, fg="white", bg="#263D42", command=OpenDir)
openFile.pack(side=RIGHT, padx=5, pady=10, anchor="nw")

listbox.bind('<<ListboxSelect>>', selected_item)
listbox.pack()

root.mainloop()
