// PROBLEMA 1: INSERCIÓN

// Inserción del Documento 1
db.videojuegos.insertOne({
  title: "The Legend of Zelda: Breath of the Wild",
  genre: ["Action", "Adventure"],
  platform: ["Nintendo Switch", "Wii U"],
  releaseYear: 2017,
  rating: 9.4,
});

// Inserción del Documento 2
db.videojuegos.insertOne({
  title: "The Witcher 3: Wild Hunt",
  genre: ["Action", "RPG"],
  platform: ["PlayStation", "Xbox", "PC"],
  releaseYear: 2015,
  rating: 9.2,
});

// Inserción del Documento 3
db.videojuegos.insertOne({
  title: "Minecraft",
  genre: ["Survival", "Adventure"],
  platform: ["PC", "PlayStation", "Xbox", "Mobile"],
  releaseYear: 2011,
  rating: 8.7,
});

// Inserción del Documento 4
db.videojuegos.insertOne({
  title: "Fortnite",
  genre: ["Battle Royale"],
  platform: ["PC", "PlayStation", "Xbox", "Mobile"],
  releaseYear: 2017,
  rating: 8.0,
});

// Inserción del Documento 5
db.videojuegos.insertOne({
  title: "Dark Souls III",
  genre: ["Action", "RPG"],
  platform: ["PlayStation", "Xbox", "PC"],
  releaseYear: 2016,
  rating: 8.9,
});

// Inserción del Documento 6
db.videojuegos.insertOne({
  title: "Red Dead Redemption 2",
  genre: ["Action", "Adventure"],
  platform: ["PlayStation", "Xbox", "PC"],
  releaseYear: 2018,
  rating: 9.8,
});

// Inserción del Documento 7
db.videojuegos.insertOne({
  title: "Super Mario Odyssey",
  genre: ["Platform"],
  platform: ["Nintendo Switch"],
  releaseYear: 2017,
  rating: 8.9,
});

// Inserción del Documento 8
db.videojuegos.insertOne({
  title: "Overwatch",
  genre: ["FPS", "Action"],
  platform: ["PlayStation", "Xbox", "PC"],
  releaseYear: 2016,
  rating: 8.5,
});

// Inserción del Documento 9
db.videojuegos.insertOne({
  title: "Grand Theft Auto V",
  genre: ["Action", "Adventure"],
  platform: ["PlayStation", "Xbox", "PC"],
  releaseYear: 2013,
  rating: 9.5,
});

// Inserción del Documento 10
db.videojuegos.insertOne({
  title: "Dota 2",
  genre: ["MOBA"],
  platform: ["PC"],
  releaseYear: 2013,
  rating: 8.4,
});

// Inserción del Documento 11
db.videojuegos.insertOne({
  title: "League of Legends",
  genre: ["MOBA"],
  platform: ["PC"],
  releaseYear: 2009,
  rating: 8.7,
});

// Inserción del Documento 12
db.videojuegos.insertOne({
  title: "Call of Duty: Modern Warfare",
  genre: ["FPS"],
  platform: ["PlayStation", "Xbox", "PC"],
  releaseYear: 2019,
  rating: 8.2,
});

// Inserción del Documento 13
db.videojuegos.insertOne({
  title: "Animal Crossing: New Horizons",
  genre: ["Simulation"],
  platform: ["Nintendo Switch"],
  releaseYear: 2020,
  rating: 8.5,
});

// Inserción del Documento 14
db.videojuegos.insertOne({
  title: "Halo 3",
  genre: ["FPS"],
  platform: ["Xbox 360"],
  releaseYear: 2007,
  rating: 9.2,
});

// Inserción del Documento 15
db.videojuegos.insertOne({
  title: "Elden Ring",
  genre: ["Action", "RPG"],
  platform: ["PlayStation", "Xbox", "PC"],
  releaseYear: 2022,
  rating: 9.5,
});

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//PROBLEMA 2: BÚSQUEDA
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// Buscar videojuegos cuyo género incluya "Action"
db.videojuegos.find({
  genre: { $in: ["Action"] },
});

// Actualizar la calificación del videojuego "Fortnite" a 8.5
db.videojuegos.updateOne({ title: "Fortnite" }, { $set: { rating: 8.5 } });

// Buscar videojuegos con calificación mayor a 9.0 y ordenarlos por año de lanzamiento de forma descendente
db.videojuegos
  .find({
    rating: { $gt: 9.0 },
  })
  .sort({
    releaseYear: -1,
  });

// Buscar videojuegos con calificación mayor a 8.7 y cuyo género incluya "Adventure"
db.videojuegos.find({
  rating: { $gt: 8.7 },
  genre: { $in: ["Adventure"] },
});

// Encontrar el videojuego con el título más largo en la colección
db.videojuegos.aggregate([
  {
    $project: {
      titleLength: { $strLenCP: "$title" }, // Calcula la longitud del título
      title: 1, // Mantiene el campo 'title' en los resultados
    },
  },
  {
    $sort: { titleLength: -1 }, // Ordena por la longitud del título de forma descendente
  },
  {
    $limit: 1, // Limita el resultado a solo un documento (el más largo)
  },
]);

// Buscar videojuegos lanzados en o después de 2017
db.videojuegos.find({
  releaseYear: { $gte: 2017 },
});

// Buscar dos videojuegos cuyo título comience con la letra "T"
db.videojuegos
  .find({
    title: { $regex: "^T", $options: "i" },
  })
  .limit(2);

// Buscar videojuegos lanzados después de 2015 y con una calificación mayor o igual a 8.5
db.videojuegos.find({
  releaseYear: { $gt: 2015 },
  rating: { $gte: 8.5 },
});

// Buscar videojuegos cuyo género incluya "RPG" y tengan plataforma "PC"
db.videojuegos.find({
  genre: { $in: ["RPG"] },
  platform: { $in: ["PC"] },
});

// Encontrar el videojuego con el menor número de plataformas
db.videojuegos.aggregate([
  {
    $project: {
      numPlatforms: { $size: "$platform" },
      title: 1,
    },
  },
  {
    $sort: { numPlatforms: 1 },
  },
  {
    $limit: 1,
  },
]);

// Buscar videojuegos cuyo género incluya "FPS" y que se lanzaron después de 2010
db.videojuegos.find({
  genre: { $in: ["FPS"] },
  releaseYear: { $gt: 2010 },
});

// Actualizar el título "The Witcher 3: Wild Hunt" para agregar un nuevo género "Fantasy"
db.videojuegos.updateOne(
  { title: "The Witcher 3: Wild Hunt" },
  { $addToSet: { genre: "Fantasy" } }
);

// Buscar videojuegos disponibles en más de una plataforma y con calificación de 9.0 o superior
db.videojuegos.find({
  platform: { $size: { $gt: 1 } },
  rating: { $gte: 9.0 },
});

// Buscar videojuegos que incluyan en su título la palabra "New"
db.videojuegos.find({
  title: { $regex: "New", $options: "i" },
});

// Encontrar el videojuego con el rating más bajo y actualizar su calificación añadiendo 0.5 puntos
let videojuego = db.videojuegos
  .find()
  .sort({ rating: 1 })
  .limit(1)
  .toArray()[0];

db.videojuegos.updateOne({ _id: videojuego._id }, { $inc: { rating: 0.5 } });

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//PROBLEMA 3: ACTUALIZACIÓN
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////

// Actualizar el número de plataformas del videojuego "Minecraft" agregando "Nintendo Switch"
db.videojuegos.updateOne(
  { title: "Minecraft" },
  { $addToSet: { platform: "Nintendo Switch" } }
);

// Actualizar el rating del videojuego "Red Dead Redemption 2" a 9.9
db.videojuegos.updateOne(
  { title: "Red Dead Redemption 2" },
  { $set: { rating: 9.9 } }
);

// Agregar el género "Strategy" al videojuego "Dota 2"
db.videojuegos.updateOne(
  { title: "Dota 2" },
  { $addToSet: { genre: "Strategy" } }
);

// Incrementar en 1 la cantidad de plataformas del videojuego "The Witcher 3: Wild Hunt" añadiendo "Nintendo Switch"
db.videojuegos.updateOne(
  { title: "The Witcher 3: Wild Hunt" },
  { $addToSet: { platform: "Nintendo Switch" } }
);

// Actualizar "Minecraft" para incluir una sinopsis descriptiva del juego
db.videojuegos.updateOne(
  { title: "Minecraft" },
  {
    $set: {
      synopsis:
        "Minecraft is a sandbox game where players can build and explore a blocky world, gather resources, craft items, and survive against letious enemies.",
    },
  }
);

// Cambiar el título de "League of Legends" a "LoL" y su año de lanzamiento a 2010
db.videojuegos.updateOne(
  { title: "League of Legends" },
  { $set: { title: "LoL", releaseYear: 2010 } }
);

// Añadir la plataforma "Nintendo Switch" a "LoL"
db.videojuegos.updateOne(
  { title: "LoL" },
  { $addToSet: { platform: "Nintendo Switch" } }
);

// Incrementar en 1 el rating de todos los videojuegos que tienen un rating inferior a 8.0
db.videojuegos.updateMany({ rating: { $lt: 8.0 } }, { $inc: { rating: 1 } });

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//PROBLEMA 4: ELIMINACIÓN
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// Eliminar el documento del videojuego con el título "Fortnite"
db.videojuegos.deleteOne({ title: "Fortnite" });

// Eliminar el campo de calificación del videojuego "Dark Souls III"
db.videojuegos.updateOne(
  { title: "Dark Souls III" },
  { $unset: { rating: "" } }
);

// Eliminar todos los videojuegos que tengan un rating inferior a 8.0
db.videojuegos.deleteMany({ rating: { $lt: 8.0 } });

// Eliminar todos los videojuegos que tengan menos de 3 plataformas
db.videojuegos.deleteMany({ platform: { $size: { $lt: 3 } } });

// Eliminar todos los videojuegos que sean del género "MOBA"
db.videojuegos.deleteMany({ genre: { $in: ["MOBA"] } });

// Eliminar el campo de género de todos los videojuegos que tengan un rating inferior a 8.0
db.videojuegos.updateMany({ rating: { $lt: 8.0 } }, { $unset: { genre: "" } });

// Eliminar todos los videojuegos lanzados antes de 2010
db.videojuegos.deleteMany({ releaseYear: { $lt: 2010 } });

// Eliminar el videojuego con el menor número de plataformas
let videojuego = db.videojuegos
  .aggregate([
    {
      $project: {
        numPlatforms: { $size: "$platform" },
        title: 1,
      },
    },
    {
      $sort: { numPlatforms: 1 },
    },
    {
      $limit: 1,
    },
  ])
  .toArray()[0];

db.videojuegos.deleteOne({ _id: videojuego._id });

///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////
//PROBLEMA 5: INDEXACIÓN
///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////

// Crear un índice de texto en el campo "title"
db.videojuegos.createIndex(
    { title: "text" }
  );
  
  // Crear un índice compuesto en los campos "genre" y "rating"
  db.videojuegos.createIndex(
    { genre: 1, rating: 1 }
  );
  
  // Crear un índice descendente en el campo "title" y ascendente en el campo "releaseYear"
  db.videojuegos.createIndex(
    { title: -1, releaseYear: 1 }
  );
  
  // Crear un índice de texto en el campo "platform"
  db.videojuegos.createIndex(
    { platform: "text" }
  );
  
///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////
//PROBLEMA 6: RELACIONES
///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////

// Insertar documentos en la colección users
db.users.insertOne({
    username: "SuperCoder123",
    first_name: "Super",
    last_name: "Coder"
  });
  
  db.users.insertOne({
    username: "TechGuru99",
    full_name: {
      first: "Tech",
      last: "Guru"
    }
  });
  
  // Insertar documentos en la colección posts
  db.posts.insertOne({
    username: "SuperCoder123",
    title: "Solves a coding challenge",
    body: "Optimizes the algorithm and achieves maximum efficiency."
  });
  
  db.posts.insertOne({
    username: "SuperCoder123",
    title: "Shares coding tutorials",
    body: "Helps aspiring coders with step-by-step guides and examples."
  });
  
  db.posts.insertOne({
    username: "TechGuru99",
    title: "Discovers a software vulnerability",
    body: "Reports it to the developers for prompt fixing."
  });
  
  db.posts.insertOne({
    username: "TechGuru99",
    title: "Creates an innovative tech product",
    body: "Introduces a groundbreaking invention to simplify everyday tasks"
  });
  
  // Insertar documentos en la colección comments
  let post1 = db.posts.findOne({ title: "Solves a coding challenge" });
  db.comments.insertOne({
    username: "SuperCoder123",
    comment: "Hope you got a good deal!",
    post: post1._id
  });
  
  let post2 = db.posts.findOne({ title: "Discovers a software vulnerability" });
  db.comments.insertOne({
    username: "SuperCoder123",
    comment: "What's mine is yours!",
    post: post2._id
  });
  
  let post3 = db.posts.findOne({ title: "Shares coding tutorials" });
  db.comments.insertOne({
    username: "SuperCoder123",
    comment: "Don't violate the licensing agreement!",
    post: post3._id
  });
  
  let post4 = db.posts.findOne({ title: "Solves a coding challenge" });
  db.comments.insertOne({
    username: "TechGuru99",
    comment: "It still isn't clean",
    post: post4._id
  });
  
  let post5 = db.posts.findOne({ title: "Shares coding tutorials" });
  db.comments.insertOne({
    username: "TechGuru99",
    comment: "Denied your PR because I found a hack",
    post: post5._id
  });
  
  // Encuentra todos los usuarios y los muestra de forma legible
db.users.find({}).pretty();

// Encuentra todas las publicaciones
db.posts.find({});

// Encuentra todas las publicaciones escritas por "SuperCoder123"
db.posts.find({ username: "SuperCoder123" });

// Encuentra todas las publicaciones escritas por "TechGuru99"
db.posts.find({ username: "TechGuru99" });

// Encuentra todos los comentarios
db.comments.find({});

// Encuentra todos los comentarios escritos por "SuperCoder123"
db.comments.find({ username: "SuperCoder123" });

// Encuentra todos los comentarios escritos por "TechGuru99"
db.comments.find({ username: "TechGuru99" });

// Encuentra todos los comentarios pertenecientes a la publicación "Shares coding tutorials"
let post = db.posts.findOne({ title: "Shares coding tutorials" });
db.comments.find({ post: post._id });

///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////
//PROBLEMA 7: CONSULTAS AVANZADAS
///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////

// Encuentra todos los videojuegos cuyo título contiene la palabra 'Legend'
db.videojuegos.find({ title: /Legend/ });

// Encuentra los videojuegos cuyo título termine con la letra 'e'
db.videojuegos.find({ title: /e$/ });

// Ordena los videojuegos encontrados por el año de lanzamiento en orden descendente
db.videojuegos.find({ title: /Legend/ }).sort({ releaseYear: -1 });

// Encuentra todos los videojuegos con más de dos géneros
db.videojuegos.find({ genre: { $size: { $gt: 2 } } });

// Filtra los videojuegos que tengan más de tres plataformas
db.videojuegos.find({ platforms: { $size: { $gt: 3 } } });

// Encuentra el videojuego con más géneros en su lista
db.videojuegos.aggregate([
  { $project: { title: 1, genreCount: { $size: "$genre" } } },
  { $sort: { genreCount: -1 } },
  { $limit: 1 }
]);

// Encuentra videojuegos cuya plataforma incluye 'PlayStation' y 'PC'
db.videojuegos.find({ platforms: { $all: ["PlayStation", "PC"] } });

// Encuentra videojuegos que tengan exactamente estas dos plataformas
db.videojuegos.find({ platforms: { $size: 2, $in: ["PlayStation", "PC"] } });

// Ordena los resultados por calificación en orden descendente
db.videojuegos.find({ platforms: { $all: ["PlayStation", "PC"] } })
  .sort({ rating: -1 });

// Encuentra videojuegos lanzados después de 2015 que sean de género 'Action' o 'RPG'
db.videojuegos.find({
  releaseYear: { $gt: 2015 },
  genre: { $in: ["Action", "RPG"] }
});

// Encuentra cuántos videojuegos cumplen esta condición
db.videojuegos.count({
  releaseYear: { $gt: 2015 },
  genre: { $in: ["Action", "RPG"] }
});

// Calcula el promedio de calificaciones para estos videojuegos
db.videojuegos.aggregate([
  { $match: { releaseYear: { $gt: 2015 }, genre: { $in: ["Action", "RPG"] } } },
  { $group: { _id: null, averageRating: { $avg: "$rating" } } }
]);

///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////
//PROBLEMA 8: OPERACIONES DE AGREGACIÓN Y AGRUPACIÓN
///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////

// 1. Encuentra el promedio de calificaciones y el total de videojuegos por género
db.videojuegos.aggregate([
    { $unwind: "$genre" },
    { $group: { _id: "$genre", averageRating: { $avg: "$rating" }, totalGames: { $sum: 1 } } }
  ]);
  
  // 2. Calcula también el año más reciente de lanzamiento por género
  db.videojuegos.aggregate([
    { $unwind: "$genre" },
    { $group: { _id: "$genre", latestReleaseYear: { $max: "$releaseYear" } } }
  ]);
  
  // 3. Encuentra los géneros con un promedio de calificación superior a 9.0
  db.videojuegos.aggregate([
    { $unwind: "$genre" },
    { $group: { _id: "$genre", averageRating: { $avg: "$rating" } } },
    { $match: { averageRating: { $gt: 9.0 } } }
  ]);
  
  // 4. Supón que cada videojuego se vende 1,000 veces. Calcula el ingreso total por plataforma
  db.videojuegos.aggregate([
    { $unwind: "$platforms" },
    { $project: { platform: "$platforms", revenue: { $multiply: [1000, "$rating"] } } },
    { $group: { _id: "$platform", totalRevenue: { $sum: "$revenue" } } }
  ]);
  
  // 5. Encuentra la plataforma que genera los mayores ingresos
  db.videojuegos.aggregate([
    { $unwind: "$platforms" },
    { $project: { platform: "$platforms", revenue: { $multiply: [1000, "$rating"] } } },
    { $group: { _id: "$platform", totalRevenue: { $sum: "$revenue" } } },
    { $sort: { totalRevenue: -1 } },
    { $limit: 1 }
  ]);
  
  // 6. Calcula también el promedio de ingresos por plataforma
  db.videojuegos.aggregate([
    { $unwind: "$platforms" },
    { $project: { platform: "$platforms", revenue: { $multiply: [1000, "$rating"] } } },
    { $group: { _id: "$platform", averageRevenue: { $avg: "$revenue" } } }
  ]);
  
  // 7. Combina las colecciones `series` y `users` para encontrar los nombres de usuarios que compraron juegos de género 'RPG'
  db.series.aggregate([
    { $match: { genre: "RPG" } },
    { $lookup: {
      from: "users",
      localField: "userId",
      foreignField: "_id",
      as: "userDetails"
    }},
    { $unwind: "$userDetails" },
    { $project: { "userDetails.first_name": 1, "userDetails.last_name": 1 } }
  ]);
  
  // 8. Encuentra los usuarios que compraron videojuegos con calificación mayor a 9.0
  db.series.aggregate([
    { $lookup: {
      from: "users",
      localField: "userId",
      foreignField: "_id",
      as: "userDetails"
    }},
    { $unwind: "$userDetails" },
    { $match: { rating: { $gt: 9.0 } } },
    { $project: { "userDetails.first_name": 1, "userDetails.last_name": 1 } }
  ]);
  
  // 9. Genera un listado de usuarios con los títulos de los videojuegos que han comprado
  db.series.aggregate([
    { $lookup: {
      from: "users",
      localField: "userId",
      foreignField: "_id",
      as: "userDetails"
    }},
    { $unwind: "$userDetails" },
    { $project: { "userDetails.first_name": 1, "userDetails.last_name": 1, title: 1 } }
  ]);
  

///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////
//PROBLEMA 9: USO DE ÍNDICES
///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////

// Crear un índice compuesto en title (texto) y releaseYear (descendente)
db.videojuegos.createIndex(
    { title: "text", releaseYear: -1 }
  );
  
  // Realizar una consulta que utilice este índice y analizar su rendimiento con explain()
  db.videojuegos.find({ title: /Legend/ }).sort({ releaseYear: -1 }).explain("executionStats");
  
  // Verificar si este índice mejora las consultas que filtran por ambos campos
  db.videojuegos.find({ title: /Legend/, releaseYear: { $gte: 2015 } }).explain("executionStats");
  
  // Usar el método explain() para analizar el uso del índice en una consulta que filtre videojuegos por palabras clave en el título
  db.videojuegos.find({ title: /Zelda/ }).explain("executionStats");
  
  // Consulta con el índice
  db.videojuegos.find({ title: /Zelda/ }).sort({ releaseYear: -1 }).explain("executionStats");
  
  // Eliminar el índice y realizar la consulta sin el índice
  db.videojuegos.dropIndex({ title: "text", releaseYear: -1 }); // Eliminar el índice
  db.videojuegos.find({ title: /Zelda/ }).sort({ releaseYear: -1 }).explain("executionStats");
  
  // Comparar el tiempo de ejecución y el número de documentos examinados
  
  // Crear un índice parcial para incluir solo los videojuegos con calificación mayor a 9.0
  db.videojuegos.createIndex(
    { title: "text", releaseYear: -1 },
    { partialFilterExpression: { rating: { $gt: 9.0 } } }
  );
  
  // Realizar una consulta que filtre videojuegos con calificación mayor a 9.0 y analizar su rendimiento
  db.videojuegos.find({ rating: { $gt: 9.0 } }).explain("executionStats");
  
  // Encontrar los videojuegos con el índice parcial que pertenezcan al género 'Adventure'
  db.videojuegos.find({ rating: { $gt: 9.0 }, genre: "Adventure" }).explain("executionStats");
  

///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////
//PROBLEMA 10: RELACIONES COMPLEJAS
///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////

// Insertar una nueva compra para un usuario existente
db.users.updateOne(
    { username: "SuperCoder123" },
    { $push: { purchaseHistory: { title: "Halo 3", genre: ["FPS"], platform: ["Xbox 360"], releaseYear: 2007, rating: 9.2 } } }
  );
  
  // Encontrar todos los usuarios que han realizado compras
  db.users.find({ "purchaseHistory": { $exists: true, $not: { $size: 0 } } });
  
  // Actualizar el historial de compras de un usuario para incluir un nuevo videojuego
  db.users.updateOne(
    { username: "TechGuru99" },
    { $push: { purchaseHistory: { title: "Elden Ring", genre: ["Action", "RPG"], platform: ["PlayStation", "Xbox", "PC"], releaseYear: 2022, rating: 9.5 } } }
  );
  
  // Insertar más comentarios relacionados con los posts de los usuarios
  db.comments.insertOne({
    username: "SuperCoder123",
    comment: "Great work on the algorithm!",
    post: ObjectId("post_obj_id")  // Reemplazar con el ObjectId de la publicación "Solves a coding challenge"
  });
  
  // Encontrar todos los comentarios realizados por un usuario específico
  db.comments.find({ username: "SuperCoder123" });
  
  // Contar el número total de comentarios por usuario
  db.comments.aggregate([
    { $group: { _id: "$username", totalComments: { $sum: 1 } } }
  ]);
  
  // Encontrar todas las publicaciones con sus respectivos comentarios
  db.posts.aggregate([
    {
      $lookup: {
        from: "comments",
        localField: "_id",
        foreignField: "post",
        as: "comments"
      }
    }
  ]);
  
  // Encontrar las publicaciones con más de dos comentarios
  db.posts.aggregate([
    {
      $lookup: {
        from: "comments",
        localField: "_id",
        foreignField: "post",
        as: "comments"
      }
    },
    { $match: { "comments": { $size: { $gt: 2 } } } }
  ]);
  
  // Ordenar las publicaciones por el número de comentarios de forma descendente
  db.posts.aggregate([
    {
      $lookup: {
        from: "comments",
        localField: "_id",
        foreignField: "post",
        as: "comments"
      }
    },
    {
      $project: {
        title: 1,
        numComments: { $size: "$comments" }
      }
    },
    { $sort: { numComments: -1 } }
  ]);
  
  
///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////
//PROBLEMA 11: PERSISTENCIA
///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////

// 1. Persiste los resultados de videojuegos agrupados por género en la colección `genre_analysis`
db.series.aggregate([
    {
      $unwind: "$genre"
    },
    {
      $group: {
        _id: "$genre",
        totalVideojuegos: { $sum: 1 },
        averagePlatforms: { $avg: { $size: "$platform" } }
      }
    },
    {
      $out: "genre_analysis"
    }
  ]);
  
  // 2. Añade también el campo de género con el número de plataformas promedio por género
  // Esto ya está incluido en el paso anterior dentro del campo `averagePlatforms`.
  
  // 3. Encuentra los géneros que tienen más de cinco videojuegos y persiste solo esos resultados
  db.genre_analysis.aggregate([
    { $match: { totalVideojuegos: { $gt: 5 } } },
    { $out: "filtered_genre_analysis" }
  ]);
  
  // 4. Exporta la colección `users` en formato JSON
  // Comando para la terminal de MongoDB:
  // mongoexport --db mongo_practica --collection users --out users.json
  
  // 5. Exporta también la colección `series` en formato JSON
  // Comando para la terminal de MongoDB:
  // mongoexport --db mongo_practica --collection series --out series.json
  
  // 6. Genera un archivo JSON con los videojuegos que tienen calificación superior a 9.0
  // Comando para la terminal de MongoDB:
  // mongoexport --db mongo_practica --collection series --query '{"rating": { "$gt": 9.0 }}' --out high_rated_video_games.json
  

///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////
//PROBLEMA 12: EJECUCIÓN DE SCRIPTS
///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////// /////////////////////////////////////////////////

/**
 * Función para buscar videojuegos según condiciones específicas
 * @param {Object} query - Condición de búsqueda (ejemplo: { genre: "Action" })
 * @param {Object} [sort] - Parámetro opcional para ordenar los resultados (ejemplo: { releaseYear: -1 })
 * @param {number} [limit] - Número máximo de resultados a devolver
 */
function buscarVideojuegos(query, sort = {}, limit = 0) {
    const cursor = db.series.find(query);

    // Si hay un parámetro de ordenación, lo aplicamos
    if (Object.keys(sort).length > 0) {
        cursor.sort(sort);
    }

    // Si hay un límite, lo aplicamos
    if (limit > 0) {
        cursor.limit(limit);
    }

    return cursor.toArray();
}

// Ejemplo de uso de la función:
// Buscar videojuegos del género "Action" ordenados por año de lanzamiento de forma descendente
const videojuegosAction = buscarVideojuegos({ genre: "Action" }, { releaseYear: -1 });

// Buscar los 5 videojuegos más recientes
const videojuegosRecientes = buscarVideojuegos({}, { releaseYear: -1 }, 5);