
//Imports a CSV file in Google Drive into the Google Sheet
function importCSVFromDrive() {
  var sheet = SpreadsheetApp.getActive().getSheetByName("Données");
  sheet.getRange('A4:U54').activate();
  sheet.getActiveRangeList().clear({contentsOnly: true, commentsOnly: true, skipFilteredRows: true});
  var fileName = 'a.csv';
  var files = findFilesInDrive(fileName);
  if(files.length === 0) {
    return;
  } else if(files.length > 1) {
    return;
  }
  var file = files[0];
  var contents = Utilities.parseCsv(file.getBlob().getDataAsString());
  var sheetName = writeDataToSheet(contents);
  SpreadsheetApp.flush()
  importCSVURLFromDrive()
  SpreadsheetApp.flush()
  Commandescopie()

//Returns files in Google Drive that have a certain name.
function findFilesInDrive(filename) {
  var files = DriveApp.getFilesByName(filename);
  var result = [];
  while(files.hasNext())
    result.push(files.next());
  return result;
}

//Inserts a new sheet and writes a 2D array of data in it
function writeDataToSheet(data) {
  var sheet = SpreadsheetApp.getActive().getSheetByName("Données")
  sheet.getRange(3, 1, data.length, data[0].length).setValues(data);
  return sheet.getName();
  
}

//Format the sheet, add the relevant information in the right place, and create two csv for printing of labels
function Commandescopie() {
  var ss = SpreadsheetApp.getActiveSpreadsheet(); 
  var sheet = ss.getSheetByName('lettermail');
  // create a folder from the name of the spreadsheet
  var folder = DriveApp.getFolderById('1FFaPuRCapBlaxPpY-GJ_tK5UGfmtVWlR');
  // append ".csv" extension to the sheet name
  fileName = sheet.getName() + ".csv";
  // convert all available sheet data to csv format
  var csvFile = convertRangeToCsvFile_(fileName, sheet);
  // create a file in the Docs List with the given name and the csv data
  var file = folder.createFile(fileName, csvFile);
  //File download
  var downloadURL = file.getDownloadUrl().slice(0, -8);

  var ss = SpreadsheetApp.getActiveSpreadsheet(); 
  var sheet = ss.getSheetByName('parcel');
  // create a folder from the name of the spreadsheet
  var folder = DriveApp.getFolderById('1ukOK3VU19pzVopWFWMgX-ZSFpHozMCWs');
  // append ".csv" extension to the sheet name
  fileName = sheet.getName() + ".csv";
  // convert all available sheet data to csv format
  var csvFile = convertRangeToCsvFile_(fileName, sheet);
  // create a file in the Docs List with the given name and the csv data
  var file = folder.createFile(fileName, csvFile);
  //File downlaod
  var downloadURL = file.getDownloadUrl().slice(0, -8)
  ;
  SpreadsheetApp.flush()
  var spreadsheet = SpreadsheetApp.getActive().getSheetByName("sheetname");
  var rows = spreadsheet.getRange('AD1').getValue();
  var lastrow = spreadsheet.getRange('AC1').getValue();
  if (lastrow == 0) {
    return;
  }
  spreadsheet.getRange(lastrow,1).setValue('Commande');
  var destinationRange = spreadsheet.getRange(lastrow,1).offset(0, 0, rows);
  spreadsheet.getRange(lastrow,1).autoFill(destinationRange, SpreadsheetApp.AutoFillSeries.DEFAULT_SERIES);
  spreadsheet.getRange(lastrow,1).offset(0, 3).activate();
  spreadsheet.getRange('AE1').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  SpreadsheetApp.flush()
  SpreadsheetApp.flush()
  spreadsheet.getCurrentCell().offset(0, 0, rows, 1).activate();
  spreadsheet.getActiveRange().copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  spreadsheet.getCurrentCell().offset(0, 13).activate();
  spreadsheet.getRange('AB1').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_NORMAL, false);
  destinationRange = spreadsheet.getActiveRange().offset(0, 0, rows);
  spreadsheet.getActiveRange().autoFill(destinationRange, SpreadsheetApp.AutoFillSeries.DEFAULT_SERIES);
  var spreadsheet = SpreadsheetApp.getActive().getSheetByName("Transactions officielles binobrick");
  spreadsheet.getRange(spreadsheet.getCurrentCell().getRow(), 1, rows, 22).activate();
  spreadsheet.getActiveRange().copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);

  
}



function convertRangeToCsvFile_(csvFileName, sheet) {
  // get available data range in the spreadsheet
  var activeRange = sheet.getDataRange();
  try {
    var data = activeRange.getValues();
    var csvFile = undefined;

    // loop through the data in the range and build a string with the csv data
    if (data.length > 1) {
      var csv = "";
      for (var row = 0; row < data.length; row++) {
        for (var col = 0; col < data[row].length; col++) {
          if (data[row][col].toString().indexOf(",") != -1) {
            data[row][col] = "\"" + data[row][col] + "\"";
          }
        }

        // join each row's columns
        // add a carriage return to end of each row, except for the last one
        if (row < data.length) {
          csv += data[row].join(",") + "\r\n";
        }
        else {
          csv += data[row];
        }
      }
      csvFile = csv;
    }
    return csvFile;
  }
  catch(err) {
    Logger.log(err);
    Browser.msgBox(err);
  }
}
}
