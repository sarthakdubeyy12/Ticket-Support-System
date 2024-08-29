const { MongoClient } = require('mongodb');

const uri = mongodb+srv://dubeysarthak47:<U5BaS0gGMpcBwjBW>@cluster0.ub8oa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0; // Replace with your connection string

const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

async function connectToDatabase() {
    try {
        await client.connect();
        console.log("Connected to MongoDB");
        const database = client.db('dubeysarthak47'); // Replace with your database name
        return database;
    } catch (err) {
        console.error(err);
    }
}

module.exports = { connectToDatabase, client };
