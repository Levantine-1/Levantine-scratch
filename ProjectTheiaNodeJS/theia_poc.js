// Load the SDK and UUID
var AWS = require('aws-sdk');
var uuid = require('uuid');
AWS.config.loadFromPath('./config.json');

var bucket = 'project-theia-test';
var photo = 'subaru1997wrc.jpg';

var rekognition = new  AWS.Rekognition();

var params = {
Image: {
   S3Object: {
   Bucket: bucket,
   Name: photo
  }
 },

};

rekognition.detectLabels(params, function(err, data) {
if (err) console.log(err, err.stack); // an error occurred
else     console.log(data);           // successful response

});