from flask import Flask, render_template, request, redirect, flash, url_for
import random

app = Flask(__name__)
app.secret_key = 'unknowk'

preguntas_respuestas = [
    # GEOGRAFIA
    {
        "pregunta": "¿Cuál es la capital de Francia?",
        "respuestas": ["París", "Londres", "Madrid", "Berlín"],
        "respuesta_correcta": "París",
        "categoria": "Geografia"
    },
    {
        "pregunta": "¿Cuál es la capital de Italia?",
        "respuestas": ["París", "Roma", "Mónaco", "Berlín"],
        "respuesta_correcta": "Berlín",
        "categoria": "Geografia"
    },
    {
        "pregunta": "¿Cuál es el río más largo de América del Sur?",
        "respuestas": [" Amazonas", "Nilo", "Misisipi", "Yangtse"],
        "respuesta_correcta": "Amazonas",
        "categoria": "Geografia"
    },
    {
        "pregunta": "¿En qué país se encuentra el monte Kilimanjaro?",
        "respuestas": ["Kenia", "Tanzania", "Sudáfrica", "Uganda"],
        "respuesta_correcta": "Tanzania",
        "categoria": "Geografia"
    },
    {
        "pregunta": "¿Cuál es el país más grande por área en América del Norte?",
        "respuestas": ["Canadá", "Estados Unidos", "México", "Groenlandia"],
        "respuesta_correcta": "Canadá",
        "categoria": "Geografia"
    },
    {
        "pregunta": "¿Cuál es el punto más alto de la Tierra?",
        "respuestas": ["Monte Kilimanjaro", "Monte Everest", "Monte Aconcagua", " Monte McKinley"],
        "respuesta_correcta": "Monte Everest",
        "categoria": "Geografia"
    },
    {
        "pregunta": "¿Cuál es el país más pequeño del mundo por área terrestre?",
        "respuestas": ["San Marino", "Mónaco", "Ciudad del Vaticano", "Liechtenstein"],
        "respuesta_correcta": "Ciudad del Vaticano",
        "categoria": "Geografia"
    },
    {
        "pregunta": "¿En qué país se encuentra el lago Titicaca?",
        "respuestas": ["Perú", "Bolivia", "Chile", "Argentina"],
        "respuesta_correcta": "Bolivia",
        "categoria": "Geografia"
    },
    {
        "pregunta": "¿Cuál es el desierto más grande del mundo?",
        "respuestas": ["Desierto del Sahara", "Desierto de Gobi", "Desierto de Kalahari", "Desierto de Atacama"],
        "respuesta_correcta": "Desierto del Sahara",
        "categoria": "Geografia"
    },
    {
        "pregunta": "¿Cuál es el océano más grande del mundo?",
        "respuestas": ["Océano Atlántico", "Océano Índico", "Océano Pacífico", "Océano Ártico"],
        "respuesta_correcta": "Océano Pacífico",
        "categoria": "Geografia"
    },
    {
        "pregunta": "¿En qué país se encuentra la Gran Muralla China?",
        "respuestas": ["Japón", "Corea del Sur", "China", "Vietnam"],
        "respuesta_correcta": "China",
        "categoria": "Geografia"
    },
    {
        "pregunta": "¿Cuál es el río más largo de Europa?",
        "respuestas": ["Danubio", "Volga", "Rin", "Támesis"],
        "respuesta_correcta": "Volga",
        "categoria": "Geografia"
    },
    {
        "pregunta": "¿En qué país se encuentra la ciudad de Petra?",
        "respuestas": ["Egipto", "Líbano", "Jordania", "Israel"],
        "respuesta_correcta": "Jordania",
        "categoria": "Geografia"
    },
    {
        "pregunta": "¿Cuál es la capital de Rusia?",
        "respuestas": ["Moscú", "San Petersburgo", "Kiev", "Minsk"],
        "respuesta_correcta": "Moscú",
        "categoria": "Geografia"
    },
    {
        "pregunta": "¿Cuál es la cordillera más larga del mundo?",
        "respuestas": ["Montañas Rocosas", "Cordillera de los Andes", "Montañas Himalayas", "Cordillera de los Alpes"],
        "respuesta_correcta": "Cordillera de los Andes",
        "categoria": "Geografia"
    },
    {
        "pregunta": "¿En qué país se encuentra el Canal de Panamá?",
        "respuestas": ["Panamá", "Colombia", "Costa Rica", "Nicaragua"],
        "respuesta_correcta": "Panamá",
        "categoria": "Geografia"
    },
    {
        "pregunta": "¿Cuál es la capital de Canadá?",
        "respuestas": ["Toronto", "Montreal", "Ottawa", "Vancouver"],
        "respuesta_correcta": "Ottawa",
        "categoria": "Geografia"
    },
    {
        "pregunta": "¿Cuál es el punto más bajo de la Tierra?",
        "respuestas": ["Mariana Trench", "Valle de la Muerte", "Mar Muerto", "Gran Zanja"],
        "respuesta_correcta": "Mar Muerto",
        "categoria": "Geografia"
    },
    {
        "pregunta": "¿Cuál es el país más pequeño de América del Sur?",
        "respuestas": ["Uruguay", "Ecuador", "Guyana", "Surinam"],
        "respuesta_correcta": "Surinam",
        "categoria": "Geografia"
    },
    {
        "pregunta": "¿En qué país se encuentra el río Misisipi?",
        "respuestas": ["Estados Unidos", "Canadá", "México", "Argentina"],
        "respuesta_correcta": "Estados Unidos",
        "categoria": "Geografia"
    },
    { 
        "pregunta": "¿Cuál es la capital de España?", 
        "respuestas": ["Madrid", "Barcelona", "Valencia", "Sevilla"], 
        "respuesta_correcta": "Madrid", 
        "categoria": "Geografia" 
    },
    { 
        "pregunta": "¿Cuál es el país más poblado del mundo?", 
        "respuestas": ["China", "India", "Estados Unidos", "Brasil"], 
        "respuesta_correcta": "China", 
        "categoria": "Geografia" 
    },
    { 
        "pregunta": "¿Cuál es la capital de Australia?", 
        "respuestas": ["Canberra", "Sídney", "Melbourne", "Brisbane"], 
        "respuesta_correcta": "Canberra", 
        "categoria": "Geografia" 
    },
    { 
        "pregunta": "¿Cuál es el país más poblado de América del Sur?", 
        "respuestas": ["Brasil", "Colombia", "Argentina", "Perú"], 
        "respuesta_correcta": "Brasil", 
        "categoria": "Geografia" 
    }, 
    { 
        "pregunta": "¿Cuál es la capital de Argentina?", 
        "respuestas": ["Buenos Aires", "Córdoba", "Rosario", "Mendoza"], 
        "respuesta_correcta": "Buenos Aires", 
        "categoria": "Geografia" 
    }, 
    { 
        "pregunta": "¿Cuál es el lago más profundo del mundo?", 
        "respuestas": ["Baikal", "Tanganica", "Caspian", "Superior"], 
        "respuesta_correcta": "Baikal", 
        "categoria": "Geografia" 
    }, 
    { 
        "pregunta": "¿Cuál es la capital de Sudáfrica?", 
        "respuestas": ["Pretoria", "Ciudad del Cabo", "Bloemfontein", "Johannesburgo"], 
        "respuesta_correcta": "Pretoria", 
        "categoria": "Geografia" 
    },
    { 
        "pregunta": "¿Cuál es el país más grande de América Central?", 
        "respuestas": ["Nicaragua", "Honduras", "Guatemala", "Costa Rica"], 
        "respuesta_correcta": "Nicaragua", 
        "categoria": "Geografia" 
    }, 
    { 
        "pregunta": "¿Cuál es la montaña más alta de Europa?", 
        "respuestas": ["Monte Elbrús", "Mont Blanc", "Matterhorn", "Cervino"], 
        "respuesta_correcta": "Monte Elbrús", 
        "categoria": "Geografia" 
    }, 
    { 
        "pregunta": "¿Cuál es la capital de Suecia?", 
        "respuestas": ["Estocolmo", "Gotemburgo", "Malmö", "Uppsala"], 
        "respuesta_correcta": "Estocolmo", 
        "categoria": "Geografia" 
    }, 
    { 
        "pregunta": "¿Cuál es el país más poblado de África?", 
        "respuestas": ["Nigeria", "Etiopía", "Egipto", "República Democrática del Congo"], 
        "respuesta_correcta": "Nigeria", 
        "categoria": "Geografia" 
    }, 
    { 
       "pregunta": "¿Cuál es el país más poblado de África por área terrestre?", 
       "respuestas": ["Nigeria", "Etiopía", "Sudáfrica", "Argelia"], 
       "respuesta_correcta": "Sudáfrica", 
       "categoria": "Geografia" 
    }, 
    { 
        "pregunta": "¿Cuál es la capital de México?", 
        "respuestas": ["Ciudad de México", "Monterrey", "Guadalajara", "Puebla"], 
        "respuesta_correcta": "Ciudad de México", 
        "categoria": "Geografia" 
    }, 
    { 
        "pregunta": "¿Cuál es la capital de Jamaica?", 
        "respuestas": ["Kingston", "Montego Bay", "Spanish Town", "Portmore"], 
        "respuesta_correcta": "Kingston", 
        "categoria": "Geografia" 
    }, 
    { 
        "pregunta": "¿Cuál es la capital de Chile?", 
        "respuestas": ["Santiago", "Valparaíso", "Concepción", "Viña del Mar"], 
        "respuesta_correcta": "Santiago", 
        "categoria": "Geografia" 
    }, 
    { 
        "pregunta": "¿Cuál es la capital de Portugal?", 
        "respuestas": ["Lisboa", "Oporto", "Funchal", "Coímbra"], 
        "respuesta_correcta": "Lisboa", 
        "categoria": "Geografia" 
    }, 
    { 
        "pregunta": "¿Cuál es el río más largo de Oceanía?", 
        "respuestas": ["Murray", "Darling", "Yarra", "Tweed"], 
        "respuesta_correcta": "Murray", 
        "categoria": "Geografia"
    },
    { 
        "pregunta": "¿Cuál es la capital de Brasil?", 
        "respuestas": ["Brasilia", "Río de Janeiro", "Sao Paulo", "Belo Horizonte"], 
        "respuesta_correcta": "Brasilia", 
        "categoria": "Geografia" 
    }, 
    { 
        "pregunta": "¿Cuál es el país más pequeño de Asia por área terrestre?", 
        "respuestas": ["Maldivas", "Singapur", "Brunéi", "Bahréin"], 
        "respuesta_correcta": "Singapur", 
        "categoria": "Geografia" 
    }, 
    { 
        "pregunta": "¿Cuál es la capital de Corea del Sur?", 
        "respuestas": ["Seúl", "Busán", "Incheon", "Daegu"], 
        "respuesta_correcta": "Seúl", 
        "categoria": "Geografia" 
    }, 
    { 
        "pregunta": "¿Cuál es el lago más grande de África?", 
        "respuestas": ["Victoria", "Tanganica", "Malawi", "Albert"], 
        "respuesta_correcta": "Victoria", 
        "categoria": "Geografia" 
    }, 
    { 
        "pregunta": "¿Cuál es la capital de Noruega?", 
        "respuestas": ["Oslo", "Bergen", "Trondheim", "Stavanger"], 
        "respuesta_correcta": "Oslo", 
        "categoria": "Geografia" 
    }, 
    { 
        "pregunta": "¿Cuál es la capital de Turquía?", 
        "respuestas": ["Ankara", "Estambul", "Antalya", "Esmirna"], 
        "respuesta_correcta": "Ankara", 
        "categoria": "Geografia" 
    }, 
    { 
        "pregunta": "¿Cuál es el país más pequeño de América del Norte por área terrestre?", 
        "respuestas": ["San Cristóbal y Nieves", "Antigua y Barbuda", "Barbados", "Santa Lucía"], 
        "respuesta_correcta": "San Cristóbal y Nieves", 
        "categoria": "Geografia" 
    }, 
    { 
        "pregunta": "¿Cuál es el país más poblado de Asia?", 
        "respuestas": ["China", "India", "Indonesia", "Pakistán"], 
        "respuesta_correcta": "China", 
        "categoria": "Geografia" 
    }, 
    { 
        "pregunta": "¿Cuál es la capital de Islandia?", 
        "respuestas": ["Reikiavik", "Akureyri", "Hafnarfjörður", "Kópavogur"], 
        "respuesta_correcta": "Reikiavik", 
        "categoria": "Geografia" 
    }, 
    { 
        "pregunta": "¿Cuál es el país más pequeño de Oceanía por área terrestre?", 
        "respuestas": ["Nauru", "Tuvalu", "Palau", "Vanuatu"], 
        "respuesta_correcta": "Nauru", 
        "categoria": "Geografia" 
    },
    { 
        "pregunta": "¿Cuál es la capital de Colombia?", 
        "respuestas": ["Bogotá", "Medellín", "Cali", "Barranquilla"], 
        "respuesta_correcta": "Bogotá", 
        "categoria": "Geografia" 
    }, 
    { 
        "pregunta": "¿Cuál es el país más pequeño de América Central por área terrestre?", 
        "respuestas": ["El Salvador", "Belice", "Costa Rica", "Panamá"], 
        "respuesta_correcta": "Belice", 
        "categoria": "Geografia" 
    }, 
    { 
        "pregunta": "¿Cuál es la capital de Nigeria?", 
        "respuestas": ["Abuja", "Lagos", "Kano", "Ibadan"], 
        "respuesta_correcta": "Abuja", 
        "categoria": "Geografia" 
    },
    # LITERATURA
    { 
        "pregunta": "¿Quién escribió 'Don Quijote de la Mancha'?", 
        "respuestas": ["Miguel de Cervantes", "Federico García Lorca", "Gabriel García Márquez", "Jorge Luis Borges"], 
        "respuesta_correcta": "Miguel de Cervantes", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Qué escritor es conocido por su obra 'Cien años de soledad'?", 
        "respuestas": ["Gabriel García Márquez", "Julio Cortázar", "Mario Vargas Llosa", "Pablo Neruda"], 
        "respuesta_correcta": "Gabriel García Márquez", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Quién escribió 'Romeo y Julieta'?", 
        "respuestas": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Fyodor Dostoevsky"], 
        "respuesta_correcta": "William Shakespeare", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Cuál es el autor de 'El principito'?", 
        "respuestas": ["Antoine de Saint-Exupéry", "Victor Hugo", "J.K. Rowling", "Leo Tolstoy"], 
        "respuesta_correcta": "Antoine de Saint-Exupéry", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Quién escribió 'La Odisea'?", 
        "respuestas": ["Homero", "Virgilio", "Ovidio", "Sófocles"], 
        "respuesta_correcta": "Homero", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Cuál es el autor de 'Orgullo y prejuicio'?", 
        "respuestas": ["Jane Austen", "Emily Brontë", "Charlotte Brontë", "Louisa May Alcott"], 
        "respuesta_correcta": "Jane Austen",
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Quién escribió '1984'?", 
        "respuestas": ["George Orwell", "Ray Bradbury", "Aldous Huxley", "Philip K. Dick"], 
        "respuesta_correcta": "George Orwell", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Qué autor escribió 'El retrato de Dorian Gray'?", 
        "respuestas": ["Oscar Wilde", "Herman Melville", "Edgar Allan Poe", "Thomas Hardy"], 
        "respuesta_correcta": "Oscar Wilde", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Quién es el autor de 'El laberinto de los espíritus'?", 
        "respuestas": ["Carlos Ruiz Zafón", "Isabel Allende", "Julio Cortázar", "Gustavo Adolfo Bécquer"], 
        "respuesta_correcta": "Carlos Ruiz Zafón", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Cuál es el autor de 'El señor de los anillos'?", 
        "respuestas": ["J.R.R. Tolkien", "C.S. Lewis", "J.K. Rowling", "George R.R. Martin"], 
        "respuesta_correcta": "J.R.R. Tolkien", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Quién escribió 'El amor en los tiempos del cólera'?", 
        "respuestas": ["Gabriel García Márquez", "Mario Vargas Llosa", "Pablo Neruda", "Jorge Luis Borges"], 
        "respuesta_correcta": "Gabriel García Márquez", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Qué autor es conocido por 'Moby Dick'?", 
        "respuestas": ["Herman Melville", "Mark Twain", "Edgar Allan Poe", "Nathaniel Hawthorne"], 
        "respuesta_correcta": "Herman Melville", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Quién escribió 'La metamorfosis'?", 
        "respuestas": ["Franz Kafka", "Leo Tolstoy", "Fyodor Dostoevsky", "Virginia Woolf"], 
        "respuesta_correcta": "Franz Kafka", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Cuál es el autor de 'Los miserables'?", 
        "respuestas": ["Victor Hugo", "Gustave Flaubert", "Honoré de Balzac", "Émile Zola"], 
        "respuesta_correcta": "Victor Hugo", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Quién escribió 'El guardián entre el centeno'?", 
        "respuestas": ["J.D. Salinger", "Ernest Hemingway", "F. Scott Fitzgerald", "John Steinbeck"], 
        "respuesta_correcta": "J.D. Salinger", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Quién escribió 'La divina comedia'?", 
        "respuestas": ["Dante Alighieri", "Giovanni Boccaccio", "Petrarca", "Niccolò Machiavelli"], 
        "respuesta_correcta": "Dante Alighieri", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Cuál es el autor de 'Anna Karenina'?", 
        "respuestas": ["Lev Tolstói", "Fiódor Dostoyevski", "Antón Chéjov", "Iván Turguénev"], 
        "respuesta_correcta": "Lev Tolstói", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Quién escribió 'El viejo y el mar'?", 
        "respuestas": ["Ernest Hemingway", "F. Scott Fitzgerald", "John Steinbeck", "William Faulkner"], 
        "respuesta_correcta": "Ernest Hemingway", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Qué autor es conocido por 'El extraño caso del Dr. Jekyll y Mr. Hyde'?", 
        "respuestas": ["Robert Louis Stevenson", "Bram Stoker", "Mary Shelley", "Oscar Wilde"], 
        "respuesta_correcta": "Robert Louis Stevenson", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Cuál es el autor de 'Matar un ruiseñor'?", 
        "respuestas": ["Harper Lee", "J.D. Salinger", "Ray Bradbury", "Truman Capote"], 
        "respuesta_correcta": "Harper Lee", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Quién escribió 'La guerra y la paz'?", 
        "respuestas": ["León Tolstói", "Fiódor Dostoyevski", "Antón Chéjov", "Iván Turguénev"], 
        "respuesta_correcta": "León Tolstói", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Cuál es el autor de 'Crónica de una muerte anunciada'?", 
        "respuestas": ["Gabriel García Márquez", "Mario Vargas Llosa", "Jorge Luis Borges", "Isabel Allende"], 
        "respuesta_correcta": "Gabriel García Márquez", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Quién escribió 'El alquimista'?", 
        "respuestas": ["Paulo Coelho", "Isabel Allende", "Gabriel García Márquez", "Jorge Luis Borges"], 
        "respuesta_correcta": "Paulo Coelho", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Cuál es el autor de 'El amor en los tiempos del cólera'?", 
        "respuestas": ["Gabriel García Márquez", "Mario Vargas Llosa", "Pablo Neruda", "Jorge Luis Borges"], 
        "respuesta_correcta": "Gabriel García Márquez", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Quién escribió 'Memorias de África'?", 
        "respuestas": ["Isak Dinesen", "Ernest Hemingway", "Karen Blixen", "John Le Carré"], 
        "respuesta_correcta": "Isak Dinesen", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Cuál es el autor de 'Las uvas de la ira'?", 
        "respuestas": ["John Steinbeck", "F. Scott Fitzgerald", "Ernest Hemingway", "William Faulkner"], 
        "respuesta_correcta": "John Steinbeck", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Quién escribió 'Moby Dick'?", 
        "respuestas": ["Herman Melville", "Mark Twain", "Edgar Allan Poe", "Nathaniel Hawthorne"], 
        "respuesta_correcta": "Herman Melville", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Cuál es el autor de 'El retrato de Dorian Gray'?", 
        "respuestas": ["Oscar Wilde", "Herman Melville", "Edgar Allan Poe", "Thomas Hardy"], 
        "respuesta_correcta": "Oscar Wilde", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Quién escribió 'El túnel'?", 
        "respuestas": ["Ernesto Sabato", "Jorge Luis Borges", "Julio Cortázar", "Gabriel García Márquez"], 
        "respuesta_correcta": "Ernesto Sabato", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Cuál es el autor de 'Los hermanos Karamázov'?", 
        "respuestas": ["Fiódor Dostoyevski", "Lev Tolstói", "Antón Chéjov", "Iván Turguénev"], 
        "respuesta_correcta": "Fiódor Dostoyevski", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Quién escribió 'El lobo estepario'?", 
        "respuestas": ["Hermann Hesse", "Franz Kafka", "Thomas Mann", "Robert Musil"], 
        "respuesta_correcta": "Hermann Hesse", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Cuál es el autor de 'El corazón de las tinieblas'?", 
        "respuestas": ["Joseph Conrad", "F. Scott Fitzgerald", "Ernest Hemingway", "William Faulkner"], 
        "respuesta_correcta": "Joseph Conrad", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Quién escribió 'El aleph'?", 
        "respuestas": ["Jorge Luis Borges", "Julio Cortázar", "Gabriel García Márquez", "Ernesto Sabato"], 
        "respuesta_correcta": "Jorge Luis Borges", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Cuál es el autor de 'Las aventuras de Sherlock Holmes'?", 
        "respuestas": ["Arthur Conan Doyle", "Agatha Christie", "Edgar Allan Poe", "G.K. Chesterton"], 
        "respuesta_correcta": "Arthur Conan Doyle", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Quién escribió 'Rayuela'?", 
        "respuestas": ["Julio Cortázar", "Jorge Luis Borges", "Gabriel García Márquez", "Mario Vargas Llosa"], 
        "respuesta_correcta": "Julio Cortázar", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Quién es el autor de 'La ciudad y los perros'?", 
        "respuestas": ["Mario Vargas Llosa", "Gabriel García Márquez", "Jorge Luis Borges", "Julio Cortázar"], 
        "respuesta_correcta": "Mario Vargas Llosa", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Qué escritor es conocido por su obra 'Fahrenheit 451'?", 
        "respuestas": ["Ray Bradbury", "George Orwell", "Aldous Huxley", "Philip K. Dick"], 
        "respuesta_correcta": "Ray Bradbury", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Quién escribió 'El amor en los tiempos del cólera'?", 
        "respuestas": ["Gabriel García Márquez", "Mario Vargas Llosa", "Pablo Neruda", "Jorge Luis Borges"], 
        "respuesta_correcta": "Gabriel García Márquez", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Cuál es el autor de 'La naranja mecánica'?", 
        "respuestas": ["Anthony Burgess", "Aldous Huxley", "Philip K. Dick", "Ray Bradbury"], 
        "respuesta_correcta": "Anthony Burgess", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Quién escribió 'La casa de los espíritus'?", 
        "respuestas": ["Isabel Allende", "Gabriel García Márquez", "Mario Vargas Llosa", "Jorge Luis Borges"], 
        "respuesta_correcta": "Isabel Allende", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Qué autor es conocido por 'El viejo y el mar'?", 
        "respuestas": ["Ernest Hemingway", "F. Scott Fitzgerald", "John Steinbeck", "William Faulkner"], 
        "respuesta_correcta": "Ernest Hemingway", 
        "categoria": "Literatura" 
    }, 
    { 
        "pregunta": "¿Quién escribió 'Drácula'?", 
        "respuestas": ["Bram Stoker", "Mary Shelley", "H.P. Lovecraft", "Edgar Allan Poe"], 
        "respuesta_correcta": "Bram Stoker", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Cuál es el autor de 'La hoguera de las vanidades'?", 
        "respuestas": ["Tom Wolfe", "John Irving", "Philip Roth", "Don DeLillo"], 
        "respuesta_correcta": "Tom Wolfe", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Quién escribió 'Los pilares de la Tierra'?", 
        "respuestas": ["Ken Follett", "George R.R. Martin", "Stephen King", "J.K. Rowling"], 
        "respuesta_correcta": "Ken Follett", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Cuál es el autor de 'Rebelión en la granja'?", 
        "respuestas": ["George Orwell", "Ray Bradbury", "Aldous Huxley", "Philip K. Dick"], 
        "respuesta_correcta": "George Orwell", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Quién escribió 'Las aventuras de Tom Sawyer'?", 
        "respuestas": ["Mark Twain", "Herman Melville", "Edgar Allan Poe", "Nathaniel Hawthorne"], 
        "respuesta_correcta": "Mark Twain", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Cuál es el autor de 'Las crónicas de Narnia'?", 
        "respuestas": ["C.S. Lewis", "J.R.R. Tolkien", "J.K. Rowling", "Philip Pullman"], 
        "respuesta_correcta": "C.S. Lewis", 
        "categoria": "Literatura" 
    }, 
    { 
        "pregunta": "¿Quién escribió 'Un mundo feliz'?", 
        "respuestas": ["Aldous Huxley", "George Orwell", "Ray Bradbury", "Philip K. Dick"], 
        "respuesta_correcta": "Aldous Huxley", 
        "categoria": "Literatura" 
    },
    { 
        "pregunta": "¿Cuál es el autor de 'El perfume'?", 
        "respuestas": ["Patrick Süskind", "Hermann Hesse", "Franz Kafka", "Thomas Mann"], 
        "respuesta_correcta": "Patrick Süskind", 
        "categoria": "Literatura" 
    }, 
    { 
        "pregunta": "¿Quién escribió 'El conde de Montecristo'?", 
        "respuestas": ["Alexandre Dumas", "Victor Hugo", "Gustave Flaubert", "Honoré de Balzac"], 
        "respuesta_correcta": "Alexandre Dumas", 
        "categoria": "Literatura" 
    },
    # HISTORIA
    { 
        "pregunta": "¿En qué año llegó Cristóbal Colón a América?", 
        "respuestas": ["1492", "1500", "1521", "1476"], 
        "respuesta_correcta": "1492", 
        "categoria": "Historia" 
    }, 
    { 
        "pregunta": "¿Qué imperio fue conquistado por los españoles bajo el liderazgo de Hernán Cortés?", 
        "respuestas": ["Imperio Azteca", "Imperio Inca", "Imperio Maya", "Imperio Romano"], 
        "respuesta_correcta": "Imperio Azteca", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿Quién fue el primer presidente de los Estados Unidos?", 
        "respuestas": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"], 
        "respuesta_correcta": "George Washington", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿En qué año comenzó la Primera Guerra Mundial?", 
        "respuestas": ["1914", "1918", "1939", "1945"], 
        "respuesta_correcta": "1914", 
        "categoria": "Historia" 
    }, 
    { 
        "pregunta": "¿Quién fue el líder de la Revolución Rusa en 1917?", 
        "respuestas": ["Vladimir Lenin", "Joseph Stalin", "Leon Trotsky", "Mikhail Gorbachev"], 
        "respuesta_correcta": "Vladimir Lenin", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿En qué año terminó la Segunda Guerra Mundial?", 
        "respuestas": ["1945", "1939", "1941", "1948"], 
        "respuesta_correcta": "1945", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿Cuál fue la batalla que puso fin al dominio napoleónico en Europa?", 
        "respuestas": ["Batalla de Waterloo", "Batalla de Trafalgar", "Batalla de Borodino", "Batalla de Austerlitz"], 
        "respuesta_correcta": "Batalla de Waterloo", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿Cuál fue el primer país en lanzar un satélite artificial al espacio?", "respuestas": ["Unión Soviética", "Estados Unidos", "China", "Alemania"], 
        "respuesta_correcta": "Unión Soviética", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿En qué año se firmó la Declaración de Independencia de los Estados Unidos?", 
        "respuestas": ["1776", "1789", "1800", "1812"], 
        "respuesta_correcta": "1776", 
        "categoria": "Historia" 
    }, 
    { 
        "pregunta": "¿Quién fue el líder de la Revolución Cubana?", 
        "respuestas": ["Fidel Castro", "Che Guevara", "Camilo Cienfuegos", "Raul Castro"], 
        "respuesta_correcta": "Fidel Castro", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿En qué año comenzó la Revolución Francesa?", 
        "respuestas": ["1789", "1799", "1815", "1830"], 
        "respuesta_correcta": "1789", 
        "categoria": "Historia" 
    }, 
    { 
        "pregunta": "¿Quién fue el primer emperador romano?", 
        "respuestas": ["César Augusto", "Julio César", "Marco Antonio", "Calígula"], 
        "respuesta_correcta": "César Augusto", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿En qué año se firmó la Constitución de los Estados Unidos?", 
        "respuestas": ["1787", "1776", "1791", "1800"], 
        "respuesta_correcta": "1787", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿Qué tratado puso fin a la Primera Guerra Mundial?", 
        "respuestas": ["Tratado de Versalles", "Tratado de Trianón", "Tratado de Brest-Litovsk", "Tratado de Saint-Germain-en-Laye"], 
        "respuesta_correcta": 
        "Tratado de Versalles", 
        "categoria": "Historia" 
    }, 
    { 
        "pregunta": "¿Quién fue el líder de la resistencia francesa durante la Segunda Guerra Mundial?", 
        "respuestas": ["Charles de Gaulle", "Winston Churchill", "Franklin D. Roosevelt", "Joseph Stalin"], 
        "respuesta_correcta": "Charles de Gaulle", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿En qué año llegaron los primeros colonos ingleses a América del Norte?", 
        "respuestas": ["1607", "1620", "1492", "1776"], 
        "respuesta_correcta": "1607", 
        "categoria": "Historia" 
    }, 
    { 
        "pregunta": "¿Quién fue el presidente de los Estados Unidos durante la Guerra Civil Americana?", 
        "respuestas": ["Abraham Lincoln", "Andrew Johnson", "Ulysses S. Grant", "Jefferson Davis"], 
        "respuesta_correcta": "Abraham Lincoln", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿En qué año se produjo la caída del Muro de Berlín?", 
        "respuestas": ["1989", "1991", "1986", "1990"], 
        "respuesta_correcta": "1989", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿Quién fue el líder de la Revolución China?", 
        "respuestas": ["Mao Zedong", "Chiang Kai-shek", "Sun Yat-sen", "Deng Xiaoping"], 
        "respuesta_correcta": "Mao Zedong", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿En qué año se firmó la Declaración de Derechos Humanos de las Naciones Unidas?", 
        "respuestas": ["1948", "1951", "1954", "1945"], 
        "respuesta_correcta": "1948", 
        "categoria": "Historia" 
    }, 
    { 
        "pregunta": "¿Quién fue el líder de la Revolución Rusa en 1917?",
        "respuestas": ["Vladimir Lenin", "Joseph Stalin", "Leon Trotsky", "Mikhail Gorbachev"], 
        "respuesta_correcta": "Vladimir Lenin", 
        "categoria": "Historia" 
    }, 
    { 
        "pregunta": "¿En qué año comenzó la Revolución Industrial?", 
        "respuestas": ["Siglo XVIII", "Siglo XIX", "Siglo XVII", "Siglo XX"], 
        "respuesta_correcta": "Siglo XVIII", 
        "categoria": "Historia" 
    }, 
    { 
        "pregunta": "¿Quién fue el primer emperador de China?", 
        "respuestas": ["Qin Shi Huang", "Han Wudi", "Emperador Wu de Han", "Kangxi"], 
        "respuesta_correcta": "Qin Shi Huang", 
        "categoria": "Historia" 
    }, 
    { 
        "pregunta": "¿Cuál fue el primer país en realizar viajes de exploración marítima en el siglo XV?", 
        "respuestas": ["Portugal", "España", "Inglaterra", "Francia"], 
        "respuesta_correcta": "Portugal", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿En qué año se produjo la Revolución de Octubre en Rusia?", 
        "respuestas": ["1917", "1918", "1916", "1920"], 
        "respuesta_correcta": "1917", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿Qué evento histórico marcó el inicio del Renacimiento en Europa?", 
        "respuestas": ["Caída del Imperio Romano de Occidente", "Descubrimiento de América", "Caída de Constantinopla", "Invención de la imprenta"], 
        "respuesta_correcta": "Caída de Constantinopla", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿Quién fue el líder de la Revolución Mexicana?", 
        "respuestas": ["Emiliano Zapata", "Francisco Villa", "Venustiano Carranza", "Porfirio Díaz"], 
        "respuesta_correcta": "Emiliano Zapata", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿En qué año se firmó el Tratado de Tordesillas?", 
        "respuestas": ["1494", "1500", "1512", "1488"], 
        "respuesta_correcta": "1494", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿Quién fue el líder de la Revolución Haitiana?", 
        "respuestas": ["Toussaint Louverture", "Jean-Jacques Dessalines", "Henri Christophe", "Pierre-Dominique Toussaint L'Ouverture"], 
        "respuesta_correcta": "Toussaint Louverture", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿En qué año se fundó la ciudad de Roma?", 
        "respuestas": ["753 a.C.", "800 a.C.", "500 a.C.", "1000 a.C."], 
        "respuesta_correcta": "753 a.C.", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿Quién fue el primer presidente de México?", 
        "respuestas": ["Guadalupe Victoria", "Benito Juárez", "Miguel Hidalgo", "Antonio López de Santa Anna"], 
        "respuesta_correcta": "Guadalupe Victoria", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿En qué siglo se produjo la Revolución Industrial?", 
        "respuestas": ["Siglo XVIII", "Siglo XIX", "Siglo XVII", "Siglo XX"], 
        "respuesta_correcta": "Siglo XVIII", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿Quién fue el primer emperador de China?", 
        "respuestas": ["Qin Shi Huang", "Han Wudi", "Emperador Wu de Han", "Kangxi"], 
        "respuesta_correcta": "Qin Shi Huang", 
        "categoria": "Historia" 
    }, 
    { 
        "pregunta": "¿Cuál fue el primer país en realizar viajes de exploración marítima en el siglo XV?", 
        "respuestas": ["Portugal", "España", "Inglaterra", "Francia"], 
        "respuesta_correcta": "Portugal", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿En qué año se produjo la Revolución de Octubre en Rusia?", 
        "respuestas": ["1917", "1918", "1916", "1920"], 
        "respuesta_correcta": "1917", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿Qué evento histórico marcó el inicio del Renacimiento en Europa?", 
        "respuestas": ["Caída del Imperio Romano de Occidente", "Descubrimiento de América", "Caída de Constantinopla", "Invención de la imprenta"], 
        "respuesta_correcta": "Caída de Constantinopla", 
        "categoria": "Historia" 
    }, 
    { 
        "pregunta": "¿Quién fue el líder de la Revolución Mexicana?", "respuestas": ["Emiliano Zapata", "Francisco Villa", "Venustiano Carranza", "Porfirio Díaz"], 
        "respuesta_correcta": "Emiliano Zapata", 
        "categoria": "Historia" 
    }, 
    { 
        "pregunta": "¿En qué año se firmó el Tratado de Tordesillas?", 
        "respuestas": ["1494", "1500", "1512", "1488"], 
        "respuesta_correcta": "1494", 
        "categoria": "Historia" 
    }, 
    { 
        "pregunta": "¿Quién fue el líder de la Revolución Haitiana?", 
        "respuestas": ["Toussaint Louverture", "Jean-Jacques Dessalines", "Henri Christophe", "Pierre-Dominique Toussaint L'Ouverture"], 
        "respuesta_correcta": "Toussaint Louverture", 
        "categoria": "Historia" 
    }, 
    { 
        "pregunta": "¿En qué año se fundó la ciudad de Roma?", 
        "respuestas": ["753 a.C.", "800 a.C.", "500 a.C.", "1000 a.C."], 
        "respuesta_correcta": "753 a.C.", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿Quién fue el primer presidente de México?", 
        "respuestas": ["Guadalupe Victoria", "Benito Juárez", "Miguel Hidalgo", "Antonio López de Santa Anna"], 
        "respuesta_correcta": "Guadalupe Victoria", 
        "categoria": "Historia" 
    }, 
    { 
        "pregunta": "¿Cuál fue el primer país en realizar viajes de exploración marítima en el siglo XV?", 
        "respuestas": ["Portugal", "España", "Inglaterra", "Francia"], 
        "respuesta_correcta": "Portugal", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿En qué año se produjo la Revolución de Octubre en Rusia?", 
        "respuestas": ["1917", "1918", "1916", "1920"], 
        "respuesta_correcta": "1917", 
        "categoria": "Historia" 
    }, 
    { 
        "pregunta": "¿Qué evento histórico marcó el inicio del Renacimiento en Europa?", 
        "respuestas": ["Caída del Imperio Romano de Occidente", "Descubrimiento de América", "Caída de Constantinopla", "Invención de la imprenta"], 
        "respuesta_correcta": "Caída de Constantinopla", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿Quién fue el líder de la Revolución Mexicana?", 
        "respuestas": ["Emiliano Zapata", "Francisco Villa", "Venustiano Carranza", "Porfirio Díaz"], 
        "respuesta_correcta": "Emiliano Zapata", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿En qué año se firmó el Tratado de Tordesillas?", 
        "respuestas": ["1494", "1500", "1512", "1488"], 
        "respuesta_correcta": "1494", 
        "categoria": "Historia" 
    }, 
    { 
        "pregunta": "¿Quién fue el líder de la Revolución Haitiana?", 
        "respuestas": ["Toussaint Louverture", "Jean-Jacques Dessalines", "Henri Christophe", "Pierre-Dominique Toussaint L'Ouverture"], 
        "respuesta_correcta": "Toussaint Louverture", 
        "categoria": "Historia" 
    }, 
    { 
        "pregunta": "¿En qué año se fundó la ciudad de Roma?", 
        "respuestas": ["753 a.C.", "800 a.C.", "500 a.C.", "1000 a.C."], 
        "respuesta_correcta": "753 a.C.", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿Quién fue el primer presidente de México?", 
        "respuestas": ["Guadalupe Victoria", "Benito Juárez", "Miguel Hidalgo", "Antonio López de Santa Anna"], 
        "respuesta_correcta": "Guadalupe Victoria", 
        "categoria": "Historia" 
    },
    { 
        "pregunta": "¿Cuál fue el primer país en realizar viajes de exploración marítima en el siglo XV?", 
        "respuestas": ["Portugal", "España", "Inglaterra", "Francia"], 
        "respuesta_correcta": "Portugal", 
        "categoria": "Historia"
    },
    # CIENCIA
    { 
        "pregunta": "¿Cuál es el elemento más abundante en la atmósfera de la Tierra?", 
        "respuestas": ["Nitrógeno", "Oxígeno", "Argón", "Dióxido de carbono"], 
        "respuesta_correcta": "Nitrógeno", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es la unidad básica de la herencia?", 
        "respuestas": ["Gen", "Cromosoma", "ADN", "RNA"], 
        "respuesta_correcta": "Gen", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Quién formuló la teoría de la relatividad?", 
        "respuestas": ["Albert Einstein", "Isaac Newton", "Stephen Hawking", "Galileo Galilei"], 
        "respuesta_correcta": "Albert Einstein", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es el planeta más grande del sistema solar?", 
        "respuestas": ["Júpiter", "Saturno", "Neptuno", "Urano"], 
        "respuesta_correcta": "Júpiter", 
        "categoria": "Ciencia" 
    }, 
    { 
        "pregunta": "¿Cuál es el ácido presente en los cítricos?", 
        "respuestas": ["Ácido cítrico", "Ácido acético", "Ácido láctico", "Ácido ascórbico"], 
        "respuesta_correcta": "Ácido cítrico", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es la unidad básica de la materia?", 
        "respuestas": ["Átomo", "Molécula", "Célula", "Electrón"], 
        "respuesta_correcta": "Átomo", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Qué tipo de energía es la energía solar?", 
        "respuestas": ["Energía renovable", "Energía no renovable", "Energía térmica", "Energía cinética"], 
        "respuesta_correcta": "Energía renovable", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es el hueso más largo del cuerpo humano?", 
        "respuestas": ["Fémur", "Húmero", "Tibia", "Fíbula"], 
        "respuesta_correcta": "Fémur",
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Qué tipo de animal es un tiburón?", 
        "respuestas": ["Pez", "Mamífero", "Ave", "Anfibio"], 
        "respuesta_correcta": "Pez", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es el proceso mediante el cual las plantas producen su propio alimento?", 
        "respuestas": ["Fotosíntesis", "Respiración", "Digestión", "Fermentación"], 
        "respuesta_correcta": "Fotosíntesis", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es el hueso más pequeño del cuerpo humano?", 
        "respuestas": ["Estribo", "Martillo", "Yunque", "Escápula"], 
        "respuesta_correcta": "Estribo", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es la capa más externa de la piel humana?", 
        "respuestas": ["Epidermis", "Dermis", "Hipodermis", "Esmalte"], 
        "respuesta_correcta": "Epidermis", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es la parte del ojo que controla la cantidad de luz que entra?", 
        "respuestas": ["Pupila", "Córnea", "Iris", "Retina"], 
        "respuesta_correcta": "Iris", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es el metal más abundante en la corteza terrestre?", 
        "respuestas": ["Aluminio", "Hierro", "Cobre", "Oro"], 
        "respuesta_correcta": "Aluminio", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es la parte del átomo que lleva una carga eléctrica positiva?", 
        "respuestas": ["Núcleo", "Electrón", "Protón", "Neutrón"], 
        "respuesta_correcta": "Protón", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es el proceso mediante el cual se forman las nubes?", 
        "respuestas": ["Condensación", "Evaporación", "Sublimación", "Precipitación"], 
        "respuesta_correcta": "Condensación", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es el animal terrestre más rápido del mundo?", 
        "respuestas": ["Guepardo", "León", "Leopardo", "Lobo"], 
        "respuesta_correcta": "Guepardo", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es la parte del cuerpo humano que produce la insulina?", 
        "respuestas": ["Páncreas", "Hígado", "Riñón", "Cerebro"], 
        "respuesta_correcta": "Páncreas", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es el metal líquido a temperatura ambiente?", 
        "respuestas": ["Mercurio", "Plomo", "Estaño", "Cadmio"], 
        "respuesta_correcta": "Mercurio", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Qué tipo de energía es la energía eólica?", 
        "respuestas": ["Energía renovable", "Energía no renovable", "Energía térmica", "Energía cinética"], 
        "respuesta_correcta": "Energía renovable", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es el proceso mediante el cual se produce la energía en las estrellas?", 
        "respuestas": ["Fusión nuclear", "Fisión nuclear", "Reacción química", "Sublimación"], 
        "respuesta_correcta": "Fusión nuclear", 
        "categoria": "Ciencia" 
    }, 
    { 
        "pregunta": "¿Cuál es el gas más abundante en la atmósfera de Venus?", 
        "respuestas": ["Dióxido de carbono", "Nitrógeno", "Oxígeno", "Helio"], 
        "respuesta_correcta": "Dióxido de carbono", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es la unidad básica de la herencia?", 
        "respuestas": ["Gen", "Cromosoma", "ADN", "ARN"], 
        "respuesta_correcta": "Gen", 
        "categoria": "Ciencia" 
    }, 
    { 
        "pregunta": "¿Cuál es el nombre del proceso mediante el cual las plantas producen su propio alimento?", 
        "respuestas": ["Fotosíntesis", "Respiración", "Digestión", "Fermentación"], 
        "respuesta_correcta": "Fotosíntesis", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es la velocidad de la luz en el vacío?", 
        "respuestas": ["299,792,458 metros por segundo", "300,000,000 metros por segundo", "299,792,458 kilómetros por segundo", "299,792,458 millas por segundo"], 
        "respuesta_correcta": "299,792,458 metros por segundo", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es el hueso más largo del cuerpo humano?", 
        "respuestas": ["Fémur", "Húmero", "Tibia", "Fíbula"], 
        "respuesta_correcta": "Fémur", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es la capa más externa de la piel humana?", 
        "respuestas": ["Epidermis", "Dermis", "Hipodermis", "Esmalte"], 
        "respuesta_correcta": "Epidermis", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es el metal líquido a temperatura ambiente?", 
        "respuestas": ["Mercurio", "Plomo", "Estaño", "Cadmio"], 
        "respuesta_correcta": "Mercurio", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Qué elemento químico tiene el símbolo 'H'?", 
        "respuestas": ["Hidrógeno", "Helio", "Hierro", "Hidrato de carbono"], 
        "respuesta_correcta": "Hidrógeno", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es el órgano más grande del cuerpo humano?", 
        "respuestas": ["Piel", "Hígado", "Cerebro", "Pulmón"], 
        "respuesta_correcta": "Piel", 
        "categoria": "Ciencia" 
    }, 
    { 
        "pregunta": "¿Qué órgano es responsable de la producción de la bilis?", 
        "respuestas": ["Hígado", "Vesícula biliar", "Páncreas", "Intestino grueso"], 
        "respuesta_correcta": "Hígado", 
        "categoria": "Ciencia" 
    }, 
    { 
        "pregunta": "¿Qué porcentaje de la superficie de la Tierra está cubierto por agua?", 
        "respuestas": ["Aproximadamente 71%", "Aproximadamente 50%", "Aproximadamente 30%", "Aproximadamente 90%"], 
        "respuesta_correcta": "Aproximadamente 71%", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es el metal más abundante en la corteza terrestre?", 
        "respuestas": ["Aluminio", "Hierro", "Cobre", "Oro"], 
        "respuesta_correcta": "Aluminio", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es la parte del átomo que lleva una carga eléctrica positiva?", 
        "respuestas": ["Protón", "Electrón", "Neutrón", "Núcleo"], 
        "respuesta_correcta": "Protón", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es la unidad básica de la materia?", 
        "respuestas": ["Átomo", "Molécula", "Célula", "Electrón"], 
        "respuesta_correcta": "Átomo", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es el proceso mediante el cual se forman las nubes?", 
        "respuestas": ["Condensación", "Evaporación", "Sublimación", "Precipitación"], 
        "respuesta_correcta": "Condensación", 
        "categoria": "Ciencia" 
    }, 
    { 
        "pregunta": "¿Cuál es el animal terrestre más rápido del mundo?", 
        "respuestas": ["Guepardo", "León", "Leopardo", "Lobo"], 
        "respuesta_correcta": "Guepardo", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es el proceso mediante el cual se produce la energía en las estrellas?", 
        "respuestas": ["Fusión nuclear", "Fisión nuclear", "Reacción química", "Sublimación"], 
        "respuesta_correcta": "Fusión nuclear", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es el gas más abundante en la atmósfera de la Tierra?", 
        "respuestas": ["Nitrógeno", "Oxígeno", "Argón", "Dióxido de carbono"], 
        "respuesta_correcta": "Nitrógeno", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es la unidad básica de la herencia?", 
        "respuestas": ["Gen", "Cromosoma", "ADN", "ARN"], 
        "respuesta_correcta": "Gen", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es el nombre del proceso mediante el cual las plantas producen su propio alimento?", 
        "respuestas": ["Fotosíntesis", "Respiración", "Digestión", "Fermentación"], 
        "respuesta_correcta": "Fotosíntesis", 
        "categoria": "Ciencia" 
    }, 
    { 
        "pregunta": "¿Cuál es la velocidad de la luz en el vacío?", 
        "respuestas": ["299,792,458 metros por segundo", "300,000,000 metros por segundo", "299,792,458 kilómetros por segundo", "299,792,458 millas por segundo"], 
        "respuesta_correcta": "299,792,458 metros por segundo", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es el hueso más largo del cuerpo humano?", 
        "respuestas": ["Fémur", "Húmero", "Tibia", "Fíbula"], 
        "respuesta_correcta": "Fémur", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es la capa más externa de la piel humana?", 
        "respuestas": ["Epidermis", "Dermis", "Hipodermis", "Esmalte"], 
        "respuesta_correcta": "Epidermis", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es el metal líquido a temperatura ambiente?", 
        "respuestas": ["Mercurio", "Plomo", "Estaño", "Cadmio"], 
        "respuesta_correcta": "Mercurio", 
        "categoria": "Ciencia" 
    }, 
    { 
        "pregunta": "¿Qué elemento químico tiene el símbolo 'H'?", 
        "respuestas": ["Hidrógeno", "Helio", "Hierro", "Hidrato de carbono"], 
        "respuesta_correcta": "Hidrógeno", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es el órgano más grande del cuerpo humano?", 
        "respuestas": ["Piel", "Hígado", "Cerebro", "Pulmón"], 
        "respuesta_correcta": "Piel", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Qué órgano es responsable de la producción de la bilis?", 
        "respuestas": ["Hígado", "Vesícula biliar", "Páncreas", "Intestino grueso"], 
        "respuesta_correcta": "Hígado", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Qué porcentaje de la superficie de la Tierra está cubierto por agua?", 
        "respuestas": ["Aproximadamente 71%", "Aproximadamente 50%", "Aproximadamente 30%", "Aproximadamente 90%"], 
        "respuesta_correcta": "Aproximadamente 71%", 
        "categoria": "Ciencia" 
    },
    { 
        "pregunta": "¿Cuál es el metal más abundante en la corteza terrestre?", 
        "respuestas": ["Aluminio", "Hierro", "Cobre", "Oro"], 
        "respuesta_correcta": "Aluminio", 
        "categoria": "Ciencia" 
    },
    # ARTE
    { 
        "pregunta": "¿Quién pintó la Mona Lisa?", 
        "respuestas": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Rembrandt"], 
        "respuesta_correcta": "Leonardo da Vinci", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Cuál es la obra más famosa de Michelangelo en el techo de la Capilla Sixtina?", 
        "respuestas": ["La creación de Adán", "La última cena", "La piedad", "El David"], 
        "respuesta_correcta": "La creación de Adán", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Quién escribió la obra de teatro 'Romeo y Julieta'?", 
        "respuestas": ["William Shakespeare", "Miguel de Cervantes", "John Milton", "Dante Alighieri"], 
        "respuesta_correcta": "William Shakespeare", 
        "categoria": "Arte" 
    }, 
    { 
        "pregunta": "¿En qué país nació el pintor surrealista Salvador Dalí?", 
        "respuestas": ["España", "Francia", "Italia", "Alemania"], 
        "respuesta_correcta": "España", 
        "categoria": "Arte" 
    }, 
    { 
        "pregunta": "¿Cuál es el período artístico caracterizado por la representación de escenas de la vida cotidiana?", 
        "respuestas": ["Realismo", "Impresionismo", "Barroco", "Renacimiento"], 
        "respuesta_correcta": "Realismo", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Quién pintó 'La noche estrellada'?", 
        "respuestas": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"], 
        "respuesta_correcta": "Vincent van Gogh", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿En qué ciudad se encuentra la famosa ópera La Scala?", 
        "respuestas": ["Milán", "Roma", "París", "Viena"], 
        "respuesta_correcta": "Milán", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Quién es considerado el padre del impresionismo?", 
        "respuestas": ["Claude Monet", "Pablo Picasso", "Vincent van Gogh", "Edgar Degas"], 
        "respuesta_correcta": "Claude Monet", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Qué artista es conocido por sus esculturas 'El pensador' y 'El beso'?", 
        "respuestas": ["Auguste Rodin", "Pablo Picasso", "Vincent van Gogh", "Salvador Dalí"], 
        "respuesta_correcta": "Auguste Rodin", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Qué movimiento artístico se caracteriza por el uso de formas geométricas y colores primarios?", 
        "respuestas": ["De Stijl", "Cubismo", "Surrealismo", "Fauvismo"], 
        "respuesta_correcta": "De Stijl", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Quién pintó 'Los girasoles'?", 
        "respuestas": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"], 
        "respuesta_correcta": "Vincent van Gogh", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Qué escultor creó la obra 'El David'?", 
        "respuestas": ["Miguel Ángel", "Leonardo da Vinci", "Pablo Picasso", "Auguste Rodin"], 
        "respuesta_correcta": "Miguel Ángel", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Cuál es la pintura más famosa de Edvard Munch?", 
        "respuestas": ["El grito", "La noche estrellada", "La última cena", "La persistencia de la memoria"], 
        "respuesta_correcta": "El grito", 
        "categoria": "Arte"
    },
    { 
        "pregunta": "¿Quién pintó 'Las Meninas'?", 
        "respuestas": ["Diego Velázquez", "Pablo Picasso", "Vincent van Gogh", "Claude Monet"], 
        "respuesta_correcta": "Diego Velázquez", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Cuál es la obra más famosa de Johannes Vermeer?", 
        "respuestas": ["La joven de la perla", "La noche estrellada", "La última cena", "La persistencia de la memoria"], 
        "respuesta_correcta": "La joven de la perla", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Quién es conocido por sus obras de arte pop como 'Campbell's Soup Cans'?", 
        "respuestas": ["Andy Warhol", "Jackson Pollock", "Roy Lichtenstein", "Keith Haring"], 
        "respuesta_correcta": "Andy Warhol", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿En qué país nació el pintor renacentista Leonardo da Vinci?", 
        "respuestas": ["Italia", "Francia", "España", "Alemania"], 
        "respuesta_correcta": "Italia", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Quién pintó 'Guernica'?", 
        "respuestas": ["Pablo Picasso", "Vincent van Gogh", "Claude Monet", "Leonardo da Vinci"], 
        "respuesta_correcta": "Pablo Picasso", 
        "categoria": "Arte" 
    }, 
    { 
        "pregunta": "¿Cuál es la obra más famosa de Gustav Klimt?", 
        "respuestas": ["El beso", "La noche estrellada", "La última cena", "La persistencia de la memoria"], 
        "respuesta_correcta": "El beso", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Quién pintó 'La persistencia de la memoria'?", 
        "respuestas": ["Salvador Dalí", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"], 
        "respuesta_correcta": "Salvador Dalí", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Qué escultor creó la escultura 'El pensador'?", 
        "respuestas": ["Auguste Rodin", "Pablo Picasso", "Vincent van Gogh", "Leonardo da Vinci"], 
        "respuesta_correcta": "Auguste Rodin", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Quién pintó 'La última cena'?", 
        "respuestas": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Claude Monet"], 
        "respuesta_correcta": "Leonardo da Vinci", 
        "categoria": "Arte" 
    }, 
    { 
        "pregunta": "¿Cuál es la escultura más famosa de Auguste Rodin?", 
        "respuestas": ["El pensador", "El beso", "La piedad", "David"], 
        "respuesta_correcta": "El pensador", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Qué pintor es conocido por sus obras de arte impresionistas como 'Mujeres en el jardín'?", 
        "respuestas": ["Claude Monet", "Pablo Picasso", "Vincent van Gogh", "Salvador Dalí"], 
        "respuesta_correcta": "Claude Monet", 
        "categoria": "Arte" 
    }, 
    { 
        "pregunta": "¿En qué ciudad se encuentra el famoso Museo del Louvre?", 
        "respuestas": ["París", "Roma", "Madrid", "Londres"], 
        "respuesta_correcta": "París", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Quién es conocido por sus esculturas como 'El pensador' y 'El beso'?", 
        "respuestas": ["Auguste Rodin", "Pablo Picasso", "Vincent van Gogh", "Salvador Dalí"], 
        "respuesta_correcta": "Auguste Rodin", 
        "categoria": "Arte" 
    }, 
    { 
        "pregunta": "¿En qué período artístico surgió la obra 'La noche estrellada' de Vincent van Gogh?", 
        "respuestas": ["Postimpresionismo", "Renacimiento", "Cubismo", "Barroco"], 
        "respuesta_correcta": "Postimpresionismo", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Qué famoso arquitecto diseñó la Casa Batlló en Barcelona?", 
        "respuestas": ["Antoni Gaudí", "Le Corbusier", "Frank Lloyd Wright", "Zaha Hadid"], 
        "respuesta_correcta": "Antoni Gaudí", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Qué pintor es conocido por sus obras de arte surrealistas como 'La persistencia de la memoria'?", 
        "respuestas": ["Salvador Dalí", "Pablo Picasso", "Vincent van Gogh", "Claude Monet"], 
        "respuesta_correcta": "Salvador Dalí", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Cuál es el movimiento artístico caracterizado por el uso de colores brillantes y formas geométricas?", 
        "respuestas": ["Fauvismo", "Expresionismo", "Cubismo", "Surrealismo"], 
        "respuesta_correcta": "Fauvismo", 
        "categoria": "Arte" 
    }, 
    { 
        "pregunta": "¿Quién es conocido por sus pinturas de lirios acuáticos?", 
        "respuestas": ["Claude Monet", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci"], 
        "respuesta_correcta": "Claude Monet", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿En qué ciudad se encuentra la famosa obra de arquitectura 'La Sagrada Familia'?", 
        "respuestas": ["Barcelona", "Roma", "París", "Madrid"], 
        "respuesta_correcta": "Barcelona", 
        "categoria": "Arte" 
    }, 
    { 
        "pregunta": "¿Quién es conocido por sus obras de arte como 'El grito'?", 
        "respuestas": ["Edvard Munch", "Pablo Picasso", "Vincent van Gogh", "Salvador Dalí"], 
        "respuesta_correcta": "Edvard Munch", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿En qué ciudad se encuentra el Museo Van Gogh?", 
        "respuestas": ["Ámsterdam", "París", "Londres", "Nueva York"], 
        "respuesta_correcta": "Ámsterdam", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Quién es conocido por sus obras de arte como 'El jardín de las delicias'?", 
        "respuestas": ["Hieronymus Bosch", "Pablo Picasso", "Vincent van Gogh", "Claude Monet"], 
        "respuesta_correcta": "Hieronymus Bosch", 
        "categoria": "Arte" 
    }, 
    { 
        "pregunta": "¿Quién es conocido por sus pinturas de latas de sopa Campbell?", 
        "respuestas": ["Andy Warhol", "Jackson Pollock", "Roy Lichtenstein", "Keith Haring"], 
        "respuesta_correcta": "Andy Warhol", 
        "categoria": "Arte"
    }, 
    { 
        "pregunta": "¿Qué movimiento artístico se caracteriza por el uso de formas abstractas y colores brillantes?", 
        "respuestas": ["Expresionismo abstracto", "Cubismo", "Pop art", "Fauvismo"], 
        "respuesta_correcta": "Expresionismo abstracto", 
        "categoria": "Arte"
    },
    { 
        "pregunta": "¿Quién es conocido por sus pinturas de mujeres con flores en el cabello?", 
        "respuestas": ["Gustav Klimt", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci"], 
        "respuesta_correcta": "Gustav Klimt", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿En qué ciudad se encuentra el famoso Museo Nacional de Arte Moderno?", 
        "respuestas": ["Nueva York", "París", "Londres", "Madrid"], 
        "respuesta_correcta": "Nueva York", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Quién es conocido por sus esculturas como 'El hombre que camina'?", 
        "respuestas": ["Alberto Giacometti", "Auguste Rodin", "Pablo Picasso", "Vincent van Gogh"], 
        "respuesta_correcta": "Alberto Giacometti", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Qué famoso pintor neerlandés es conocido por sus autorretratos?", 
        "respuestas": ["Vincent van Gogh", "Rembrandt", "Johannes Vermeer", "Hieronymus Bosch"], 
        "respuesta_correcta": "Rembrandt", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Cuál es la obra más famosa de Salvador Dalí?", 
        "respuestas": ["La persistencia de la memoria", "El grito", "La última cena", "La noche estrellada"], 
        "respuesta_correcta": "La persistencia de la memoria", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Qué pintor es conocido por su técnica de puntillismo?", 
        "respuestas": ["Georges Seurat", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"], 
        "respuesta_correcta": "Georges Seurat", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Cuál es la escultura más famosa de Michelangelo?", 
        "respuestas": ["David", "El beso", "El pensador", "La piedad"], 
        "respuesta_correcta": "David", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿En qué país nació el pintor renacentista Rafael?", 
        "respuestas": ["Italia", "Francia", "España", "Alemania"], 
        "respuesta_correcta": "Italia", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Quién es conocido por sus esculturas como 'El hombre vitruviano'?", 
        "respuestas": ["Leonardo da Vinci", "Auguste Rodin", "Pablo Picasso", "Vincent van Gogh"], 
        "respuesta_correcta": "Leonardo da Vinci", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿En qué siglo vivió el pintor Johannes Vermeer?", 
        "respuestas": ["Siglo XVII", "Siglo XVI", "Siglo XVIII", "Siglo XIX"], 
        "respuesta_correcta": "Siglo XVII", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Qué movimiento artístico se caracteriza por la representación de objetos y paisajes de manera precisa y detallada?", 
        "respuestas": ["Hiperrealismo", "Expresionismo", "Surrealismo", "Cubismo"], 
        "respuesta_correcta": "Hiperrealismo", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Quién es conocido por sus obras de arte como 'La joven de la perla'?", 
        "respuestas": ["Johannes Vermeer", "Pablo Picasso", "Vincent van Gogh", "Claude Monet"], 
        "respuesta_correcta": "Johannes Vermeer", 
        "categoria": "Arte" 
    },
    { 
        "pregunta": "¿Cuál es la obra más famosa de René Magritte?", 
        "respuestas": ["La traición de las imágenes", "El hijo del hombre", "El gran masturbador", "Los amantes"], 
        "respuesta_correcta": "La traición de las imágenes", 
        "categoria": "Arte"
    },
    # DEPORTE
    { 
        "pregunta": "¿En qué deporte se utiliza una pala para golpear una pelota sobre una red?", 
        "respuestas": ["Tenis", "Pádel", "Bádminton", "Ping pong"], 
        "respuesta_correcta": "Pádel", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Cuál es el deporte más popular en Brasil?", 
        "respuestas": ["Fútbol", "Voleibol", "Baloncesto", "Tenis"], 
        "respuesta_correcta": "Fútbol", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Quién es el máximo goleador de la historia del fútbol?", 
        "respuestas": ["Pelé", "Lionel Messi", "Cristiano Ronaldo", "Diego Maradona"], 
        "respuesta_correcta": "Pelé", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Cuál es el deporte nacional de Japón?", 
        "respuestas": ["Sumo", "Judo", "Karate", "Béisbol"], 
        "respuesta_correcta": "Sumo", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Qué equipo ganó la última Copa Mundial de la FIFA?", 
        "respuestas": ["Francia", "Brasil", "Alemania", "Argentina"], 
        "respuesta_correcta": "Francia", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Qué deporte se juega en un campo dividido en nueve entradas?", 
        "respuestas": ["Béisbol", "Críquet", "Rugby", "Golf"], 
        "respuesta_correcta": "Béisbol", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Quién ganó el último Super Bowl?", 
        "respuestas": ["Tampa Bay Buccaneers", "Kansas City Chiefs", "New England Patriots", "Los Angeles Rams"], 
        "respuesta_correcta": "Tampa Bay Buccaneers", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿En qué deporte se puede ganar una medalla de oro en los Juegos Olímpicos con un 'Triple Axel'?", 
        "respuestas": ["Patinaje artístico", "Natación", "Atletismo", "Gimnasia"], 
        "respuesta_correcta": "Patinaje artístico", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Quién es considerado el mejor jugador de baloncesto de todos los tiempos?", 
        "respuestas": ["Michael Jordan", "LeBron James", "Kobe Bryant", "Magic Johnson"], 
        "respuesta_correcta": "Michael Jordan", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Cuál es el deporte más popular en Estados Unidos?", 
        "respuestas": ["Fútbol americano", "Béisbol", "Baloncesto", "Hockey sobre hielo"], 
        "respuesta_correcta": "Fútbol americano", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Qué jugador ha ganado más títulos de Grand Slam en tenis masculino?", 
        "respuestas": ["Roger Federer", "Rafael Nadal", "Novak Djokovic", "Pete Sampras"], 
        "respuesta_correcta": "Roger Federer", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿En qué año se celebró el primer Mundial de Fútbol?", 
        "respuestas": ["1930", "1950", "1970", "1990"], 
        "respuesta_correcta": "1930", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Quién es el máximo goleador en la historia de la NBA?", 
        "respuestas": ["Kareem Abdul-Jabbar", "LeBron James", "Michael Jordan", "Kobe Bryant"], 
        "respuesta_correcta": "LeBron James", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿En qué deporte se utiliza una raqueta para golpear una pelota contra una pared frontal?", 
        "respuestas": ["Squash", "Tenis", "Frontón", "Bádminton"], 
        "respuesta_correcta": "Squash", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Cuál es el récord mundial de velocidad en los 100 metros lisos masculino?", 
        "respuestas": ["9,58 segundos", "9,63 segundos", "9,69 segundos", "9,74 segundos"], 
        "respuesta_correcta": "9,58 segundos", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Quién es el actual campeón de la Liga de Campeones de la UEFA?", 
        "respuestas": ["Chelsea", "Manchester City", "Bayern Munich", "Liverpool"], 
        "respuesta_correcta": "Manchester City", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿En qué país se originó el deporte del rugby?", 
        "respuestas": ["Inglaterra", "Nueva Zelanda", "Australia", "Sudáfrica"], 
        "respuesta_correcta": "Inglaterra", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Quién es el máximo goleador en la historia del fútbol argentino?", 
        "respuestas": ["Lionel Messi", "Diego Maradona", "Gabriel Batistuta", "Hernán Crespo"], 
        "respuesta_correcta": "Lionel Messi", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Cuál es el deporte más practicado en Australia?", 
        "respuestas": ["Críquet", "Rugby", "AFL (Australian Football League)", "Natación"], 
        "respuesta_correcta": "AFL (Australian Football League)", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Quién es considerado el mejor nadador de todos los tiempos?", 
        "respuestas": ["Michael Phelps", "Ian Thorpe", "Mark Spitz", "Ryan Lochte"], 
        "respuesta_correcta": "Michael Phelps", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Cuál es el deporte nacional de Canadá?", 
        "respuestas": ["Hockey sobre hielo", "Lacrosse", "Béisbol", "Fútbol"], 
        "respuesta_correcta": "Hockey sobre hielo", 
        "categoria": "Deporte" 
    }, 
    { 
        "pregunta": "¿Quién es el máximo ganador del Tour de Francia?", 
        "respuestas": ["Eddy Merckx", "Lance Armstrong", "Chris Froome", "Bernard Hinault"], 
        "respuesta_correcta": "Eddy Merckx", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿En qué deporte se utiliza un octógono como área de combate?", 
        "respuestas": ["Artes marciales mixtas (MMA)", "Boxeo", "Kickboxing", "Muay Thai"], 
        "respuesta_correcta": "Artes marciales mixtas (MMA)", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Cuál es el deporte más popular en la India?", 
        "respuestas": ["Críquet", "Hockey sobre hierba", "Fútbol", "Tenis"], 
        "respuesta_correcta": "Críquet", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Quién es el máximo goleador de la selección argentina de fútbol?", 
        "respuestas": ["Lionel Messi", "Gabriel Batistuta", "Diego Maradona", "Sergio Agüero"], 
        "respuesta_correcta": "Lionel Messi", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Cuál es el deporte nacional de Escocia?", 
        "respuestas": ["Golf", "Rugby", "Tenis", "Curling"], 
        "respuesta_correcta": "Golf", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Quién ganó la medalla de oro en los Juegos Olímpicos de Río 2016 en la competencia de salto de pértiga masculino?", 
        "respuestas": ["Thiago Braz da Silva", "Renaud Lavillenie", "Sam Kendricks", "Armand Duplantis"], 
        "respuesta_correcta": "Thiago Braz da Silva", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Cuál es el deporte más popular en Sudáfrica?", 
        "respuestas": ["Rugby", "Fútbol", "Críquet", "Atletismo"], 
        "respuesta_correcta": "Rugby", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Quién es el máximo goleador en la historia de la selección brasileña de fútbol?", 
        "respuestas": ["Pelé", "Ronaldo", "Romário", "Neymar"], 
        "respuesta_correcta": "Pelé", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿En qué deporte se utiliza una vara para saltar obstáculos?", 
        "respuestas": ["Atletismo (Salto de altura)", "Equitación", "Polo", "Pentatlón moderno"], 
        "respuesta_correcta": "Atletismo (Salto de altura)", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Cuál es el deporte más popular en España?", 
        "respuestas": ["Fútbol", "Baloncesto", "Tenis", "Ciclismo"], 
        "respuesta_correcta": "Fútbol", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Quién es el máximo goleador de la selección española de fútbol?", 
        "respuestas": ["David Villa", "Raúl González", "Fernando Torres", "David Silva"], 
        "respuesta_correcta": "David Villa", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Cuál es el deporte nacional de Irlanda?", 
        "respuestas": ["Hurling", "Fútbol gaélico", "Rugby", "Críquet"], 
        "respuesta_correcta": "Hurling", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿En qué deporte se compite por la 'Copa Stanley'?", 
        "respuestas": ["Hockey sobre hielo", "Fútbol americano", "Baloncesto", "Béisbol"], 
        "respuesta_correcta": "Hockey sobre hielo", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Cuál es el deporte más popular en Italia?", 
        "respuestas": ["Fútbol", "Baloncesto", "Ciclismo", "Voleibol"], 
        "respuesta_correcta": "Fútbol", 
        "categoria": "Deporte" 
    }, 
    { 
        "pregunta": "¿Quién es el máximo goleador en la historia de la Premier League inglesa?", 
        "respuestas": ["Alan Shearer", "Wayne Rooney", "Thierry Henry", "Andy Cole"], 
        "respuesta_correcta": "Alan Shearer", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿En qué deporte se utiliza una pala y una pelota con agujeros?", 
        "respuestas": ["Pickleball", "Pádel", "Tenis", "Squash"], 
        "respuesta_correcta": "Pickleball", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Cuál es el deporte nacional de Canadá de verano?", 
        "respuestas": ["Lacrosse", "Fútbol", "Atletismo", "Béisbol"], 
        "respuesta_correcta": "Lacrosse", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿En qué deporte se utiliza una malla para atrapar una pelota?", 
        "respuestas": ["Béisbol", "Voleibol", "Balonmano", "Bádminton"], 
        "respuesta_correcta": "Voleibol", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Quién es el máximo goleador en la historia del Barcelona?", 
        "respuestas": ["Lionel Messi", "César Rodríguez", "Luis Suárez", "Samuel Eto'o"], 
        "respuesta_correcta": "Lionel Messi", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Cuál es el deporte más popular en Argentina?", 
        "respuestas": ["Fútbol", "Rugby", "Hockey sobre hierba", "Tenis"], 
        "respuesta_correcta": "Fútbol", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Quién es el máximo goleador en la historia del Real Madrid?", 
        "respuestas": ["Cristiano Ronaldo", "Raúl González", "Alfredo Di Stefano", "Karim Benzema"], 
        "respuesta_correcta": "Cristiano Ronaldo", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Cuál es el deporte más popular en China?", 
        "respuestas": ["Ping pong", "Fútbol", "Baloncesto", "Natación"], 
        "respuesta_correcta": "Ping pong", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Quién es el actual campeón de la NBA?", 
        "respuestas": ["Milwaukee Bucks", "Los Angeles Lakers", "Golden State Warriors", "Toronto Raptors"], 
        "respuesta_correcta": "Golden State Warriors", 
        "categoria": "Deporte"
    },
    { 
        "pregunta": "¿En qué deporte se utiliza un tablero y una canasta?", 
        "respuestas": ["Baloncesto", "Béisbol", "Hockey sobre hielo", "Voleibol"], 
        "respuesta_correcta": "Baloncesto", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Quién ganó la medalla de oro en fútbol masculino en los Juegos Olímpicos de Tokio 2020?", 
        "respuestas": ["Argentina", "Brasil", "España", "Francia"], 
        "respuesta_correcta": "Brasil", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿En qué deporte se compite por la 'Copa Davis'?", 
        "respuestas": ["Tenis", "Golf", "Fútbol", "Baloncesto"],
        "respuesta_correcta": "Tenis", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Cuál es el deporte más popular en Rusia?", 
        "respuestas": ["Fútbol", "Hockey sobre hielo", "Atletismo", "Baloncesto"], 
        "respuesta_correcta": "Fútbol", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Quién es el máximo goleador en la historia del PSG?", 
        "respuestas": ["Edinson Cavani", "Zlatan Ibrahimovic", "Kylian Mbappé", "Pauleta"], 
        "respuesta_correcta": "Edinson Cavani", 
        "categoria": "Deporte" 
    },
    { 
        "pregunta": "¿Cuál es el deporte nacional de Nueva Zelanda?", 
        "respuestas": ["Rugby", "Críquet", "Baloncesto", "Fútbol"], 
        "respuesta_correcta": "Rugby", 
        "categoria": "Deporte" 
    },
    # ALGEBRA
    { 
        "pregunta": "¿Cuál es el resultado de (3^2) + (4^2)?", 
        "respuestas": ["7", "9", "16", "25"], 
        "respuesta_correcta": "25", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de √(25)?", 
        "respuestas": ["3", "4", "5", "6"], 
        "respuesta_correcta": "5", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (2 * 3) + (4 * 5)?", 
        "respuestas": ["14", "22", "26", "32"], 
        "respuesta_correcta": "26", 
        "categoria": "Algebra" 
    },
    { 
        "pregunta": "¿Cuál es el resultado de (5 + 3)^2?", 
        "respuestas": ["64", "36", "25", "16"], 
        "respuesta_correcta": "64", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de √(36) - 2?", 
        "respuestas": ["2", "4", "5", "6"], 
        "respuesta_correcta": "4", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (4^2) - (3^2)?", 
        "respuestas": ["1", "5", "7", "9"], 
        "respuesta_correcta": "7", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (6 + 2)^2?", 
        "respuestas": ["36", "64", "100", "128"], 
        "respuesta_correcta": "64", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de √(81) + 5?", 
        "respuestas": ["15", "16", "14", "19"], 
        "respuesta_correcta": "14", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (9 - 5)^2?", 
        "respuestas": ["4", "16", "20", "25"], 
        "respuesta_correcta": "16", 
        "categoria": "Algebra"
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (5^2) - (3^2)?", 
        "respuestas": ["4", "16", "8", "12"], 
        "respuesta_correcta": "16", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (2 * 4) + (3 * 5)?", 
        "respuestas": ["16", "23", "26", "32"], 
        "respuesta_correcta": "23", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (6 + 3)^2?", 
        "respuestas": ["36", "64", "81", "100"], 
        "respuesta_correcta": "81", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de √(49) - 3?", 
        "respuestas": ["2", "4", "5", "6"], 
        "respuesta_correcta": "4", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (8^2) - (7^2)?", 
        "respuestas": ["1", "5", "7", "15"], 
        "respuesta_correcta": "15", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (7 + 3)^2?", 
        "respuestas": ["36", "64", "100", "128"], 
        "respuesta_correcta": "100", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de √(100) + 5?", 
        "respuestas": ["5", "10", "15", "20"], 
        "respuesta_correcta": "15", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (9 - 6)^2?", 
        "respuestas": ["3", "9", "15", "36"], 
        "respuesta_correcta": "9", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (6^2) - (4^2)?", 
        "respuestas": ["4", "8", "20", "32"], 
        "respuesta_correcta": "20", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (4 * 6) + (5 * 7)?", 
        "respuestas": ["34", "46", "59", "70"], 
        "respuesta_correcta": "59", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (8 + 4)^2?", 
        "respuestas": ["144", "196", "256", "324"], 
        "respuesta_correcta": "144", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de √(121) - 11?", 
        "respuestas": ["0", "1", "2", "11"], 
        "respuesta_correcta": "0", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (11^2) - (9^2)?", 
        "respuestas": ["39", "42", "38", "40"], 
        "respuesta_correcta": "40", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (10 + 4)^2?", 
        "respuestas": ["196", "256", "324", "400"], 
        "respuesta_correcta": "196", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de √(144) + 6?", 
        "respuestas": ["12", "15", "18", "21"], 
        "respuesta_correcta": "18", 
        "categoria": "Algebra" 
    },
    { 
        "pregunta": "¿Cuál es el resultado de (2^3) + (3^2)?", 
        "respuestas": ["14", "12", "13", "17"], 
        "respuesta_correcta": "17", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de √(64)?", 
        "respuestas": ["6", "7", "8", "9"], 
        "respuesta_correcta": "8", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (3 * 4) + (5 * 6)?", 
        "respuestas": ["28", "34", "42", "48"], 
        "respuesta_correcta": "42", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (4 + 5)^2?", 
        "respuestas": ["81", "90", "99", "108"], 
        "respuesta_correcta": "81", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de √(121) - 3?", 
        "respuestas": ["8", "9", "10", "11"], 
        "respuesta_correcta": "8", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (5^2) - (4^2)?", 
        "respuestas": ["5", "9", "13", "17"], 
        "respuesta_correcta": "9", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (6 + 4)^2?", 
        "respuestas": ["80", "90", "100", "110"], 
        "respuesta_correcta": "100", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de √(144) + 7?", 
        "respuestas": ["15", "16", "17", "19"], 
        "respuesta_correcta": "19", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (9 - 7)^2?", 
        "respuestas": ["2", "8", "6", "4"], 
        "respuesta_correcta": "4", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (7^2) - (6^2)?", 
        "respuestas": ["7", "13", "19", "25"], 
        "respuesta_correcta": "13", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (8 * 5) + (9 * 4)?", 
        "respuestas": ["61", "66", "71", "76"], 
        "respuesta_correcta": "76", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (5 + 6)^2?", 
        "respuestas": ["110", "121", "132", "143"], 
        "respuesta_correcta": "121", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de √(169) - 8?", 
        "respuestas": ["4", "5", "6", "7"], 
        "respuesta_correcta": "5", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (10^2) - (8^2)?", 
        "respuestas": ["26", "36", "32", "40"], 
        "respuesta_correcta": "36", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (11 + 7)^2?", 
        "respuestas": ["324", "361", "400", "441"], 
        "respuesta_correcta": "324", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de √(196) + 9?", 
        "respuestas": ["22", "18", "23", "20"], 
        "respuesta_correcta": "23", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (12 - 8)^2?", 
        "respuestas": ["16", "20", "24", "28"], 
        "respuesta_correcta": "16", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (8^2) - (5^2)?", 
        "respuestas": ["39", "31", "13", "15"], 
        "respuesta_correcta": "39", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (6 * 7) + (8 * 9)?", 
        "respuestas": ["114", "116", "126", "136"], 
        "respuesta_correcta": "114", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (9 + 8)^2?", 
        "respuestas": ["289", "324", "361", "400"], 
        "respuesta_correcta": "289", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de √(225) - 10?", 
        "respuestas": ["5", "11", "12", "13"], 
        "respuesta_correcta": "5", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (13^2) - (11^2)?", 
        "respuestas": ["42", "44", "46", "48"], 
        "respuesta_correcta": "48", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de (14 + 9)^2?", 
        "respuestas": ["529", "576", "625", "676"], 
        "respuesta_correcta": "529", 
        "categoria": "Algebra" 
    }, 
    { 
        "pregunta": "¿Cuál es el resultado de √(324) + 11?", 
        "respuestas": ["18", "29", "20", "21"], 
        "respuesta_correcta": "29", 
        "categoria": "Algebra"
    },
]

categorias = {
    "Geografia": "static/img/geografia.png",
    "Literatura": "static/img/literatura.png",
    "Historia": "static/img/historia.png",
    "Ciencia": "static/img/ciencia.png",
    "Arte": "static/img/arte.png",
    "Deporte": "static/img/deporte.png",
    "Algebra": "static/img/algebra.png"
}

categorias_disponibles = list(categorias.keys())

puntuacion = 0

preguntas_disponibles = preguntas_respuestas.copy()

@app.route('/') 
def index(): 
    global puntuacion     
    global preguntas_disponibles

    categoria_seleccionada = request.args.get('categoria') 

    if categoria_seleccionada:
        preguntas_disponibles_categoria = [preguntar for preguntar in preguntas_disponibles if preguntar['categoria'] == categoria_seleccionada]
    else:
        preguntas_disponibles_categoria = preguntas_disponibles 

    if not preguntas_disponibles:
        flash('Ya has respondido todas las preguntas.','success') 
        return render_template('index.html', pregunta=None, respuesta_correcta=None, icono_categoria=None, categoria_aleatoria=None, puntuacion=puntuacion)

    pregunta = random.choice(preguntas_disponibles_categoria) 
    respuesta_correcta = pregunta['respuesta_correcta'] 
    icono_categoria = categorias[pregunta['categoria']]
    random.shuffle(pregunta['respuestas'])
    preguntas_disponibles.remove(pregunta)
    return render_template('index.html', pregunta=pregunta, respuesta_correcta=respuesta_correcta, icono_categoria=icono_categoria, categoria_aleatoria=pregunta['categoria'], puntuacion=puntuacion)

@app.route('/comprobar', methods=['post'])
def comprobar():
    global puntuacion
    respuesta_usuario = request.form['respuesta']
    respuesta_correcta = request.form['respuesta_correcta']

    if respuesta_usuario == respuesta_correcta:
        flash("Respuesta Correcta!", 'success')
        puntuacion += 100
    else:
        flash(f"La respuesta correcta es: {respuesta_correcta}", 'danger')
        if puntuacion <= 0:
            puntuacion = 0
        else:
            puntuacion -= 50
    return redirect('/')

@app.route('/timeout')
def timeout():
    flash("Se te acabo el tiempo", "danger")
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)