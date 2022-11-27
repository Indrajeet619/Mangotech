var fs = require("fs");
import S3 from "aws-sdk/clients/s3.js";
const express = require("express");
const cors = require("cors");
var AWS = require('aws-sdk'); 
const querystring = require('querystring');
const { Curl } = require('node-libcurl');

const curl = new Curl();
const close = curl.close.bind(curl);

curl.setOpt(Curl.option.URL, '127.0.0.1/upload');
curl.setOpt(Curl.option.POST, true)
curl.setOpt(Curl.option.POSTFIELDS, querystring.stringify({
  field: 'value',
}));

curl.on('end', close);
curl.on('error', close);
var input=Curl.option.POSTFIELDS;
const value = JSON.stringify(input);
var writeStream = fs.createWriteStream("Device1.txt");
writeStream.write(value);
writeStream.end();

const accessKeyId = "secret";
const secretAccessKey = "secret";
const endpoint = "https://gateway.storjshare.io";

const s3 = new S3({
  accessKeyId,
  secretAccessKey,
  endpoint,
  s3ForcePathStyle: true,
  signatureVersion: "v4",
  connectTimeout: 0,
  httpOptions: { timeout: 0 }
});
(async () => {  
    const params = {
      Bucket: "demo1",
      Key: "my-object",
      Body: Device1.txt
    };
  
    await s3.upload(params, {
      partSize: 64 * 1024 * 1024
    }).promise();
    cd(Device1.txt);
  })();


function cd(y)
{ y1=fs.readFileSync(y,'utf8');
  let temp, hum, co;
  temp=y1.temperature;
  hum=y1.humidity;
  co=y1.co;
  if (temp>28 || hum>59 || co> 620)
  {
  var params = {
    Destination: { /* required */
      CcAddresses: [
      ],
      ToAddresses: [
        'email',
        /* more items */
      ]
    },
    Message: { /* required */
      Body: {    
      Html: {
        Charset: "UTF-8",
        Data: y
       }
       },
       Subject: {
        Charset: 'UTF-8',
        Data: y
       }
      },
    Source: 'email', /* required */
    ReplyToAddresses: [
  
    ],
  };
  
  var sendPromise = new AWS.SES({apiVersion: '2010-12-01'}).sendEmail(params).promise();
  sendPromise.then(
    function(data) {
    }).catch(
      function(err) {
     // console.error(err, err.stack);
    });
  }
  }

  
