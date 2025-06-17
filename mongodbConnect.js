const { MongoClient, ServerApiVersion } = require('mongodb');

const uri = "mongodb+srv://sanjaynesan007:sanjay2005@carrental.8yyhvxe.mongodb.net/?retryWrites=true&w=majority&appName=carrental";
// 🔁 Replace <db_password> with your actual MongoDB Atlas password.

const client = new MongoClient(uri, {
  serverApi: {
    version: ServerApiVersion.v1
    // strict: true,
    // deprecationErrors: true
  }
});


async function run() {
  try {
    await client.connect();
    await client.db("admin").command({ ping: 1 });
    console.log("✅ Connected to MongoDB successfully!");
  } finally {
    await client.close();
  }
}
run().catch(console.dir);
