const express = require("express");
const dotenv = require("dotenv/config"); //for accessing the env variable
const morgan = require("morgan"); //for logiing the endpoint access history
const connectDB = require("./Config/dbConnection");
const errorHandaler = require("./Middleware/errorHandaler");
const cors = require("cors"); //for trust cross origin platform access our api
const mongoose = require("mongoose");

// keep this under your error handler

const app = express();

//DB Connection
connectDB();

//middleware
app.use(cors()); //for trust any other origin frontend during accessing our api
app.options("*", cors()); //for trust all(*) http options during accessing our api

app.use(morgan("tiny")); //log endpoint history
app.use(express.json()); //inbuilt request body parser to json

app.use("/category", require("./Routes/categoryRoutes.js"));
app.use("/product", require("./Routes/productRoutes.js"));
app.use("/user", require("./Routes/userRoutes.js"));
app.use("/order", require("./Routes/orderRoutes.js"));
//For fetching uploaded Images
// app.use("/public/upload", express.static(__dirname + "/public/upload"));
app.use("/public/upload", express.static("/public/upload"));
//handle error -> this should be the last line in middleware section
app.use(errorHandaler);

//Testing Homepage

app.get(["/", "/myLogs"], async (req, res) => {
  const log_tbl = mongoose.models.server_logs|| mongoose.model(
    "server_logs",
    new mongoose.Schema({ name: String })
  );
  const log_data = await log_tbl.find();
  res
    .status(201)
    .json({
      msg: "Homepage Configure Perfectly! Below Are Log Data(Designed By SK Asif Iqbal)",
      length:log_data.length,
      Data: log_data,
    });
});

//Driver Code
app.listen(process.env.PORT, () => {
  console.log(
    `Application Running Successfully in : http://localhost:${process.env.PORT}`
  );
});
