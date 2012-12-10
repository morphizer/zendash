$(document).ready(function () {
    var oTable = $('#events').dataTable({
        "fnRowCallback": function(nRow, aData, iDisplayIndex){
            if (aData['severity'] == "5"){
                nRow.className = 'severity_5';
            } else if (aData['severity'] === "4"){
                nRow.className = 'severity_4';
            } else if (aData['severity'] === "3"){
                nRow.className = 'severity_3';
            } else if (aData['severity'] === "2"){
                nRow.className = 'severity_2';
            } else if (aData['severity'] === "1"){
                nRow.className = 'severity_1';
            }
            return nRow; 
        },
        "bProcessing": true,
        "bPaginate": false,
        "sAjaxSource": '/dashboard/getevents/',
        "sAjaxDataProp": "events",
        "sScrollY": "85%",
        "oLanguage": {
            "sEmptyTable": "No events to display!",
        },
        "sDom": 'rt<"bottom"filp><"clear">',
        "aoColumns": [
            { "mData": "severity", "bVisible": false },
            { "mData": "count", "sWidth": "5%" },
            { "mData": "device.text" },
            { "mData": "component.text" },
            { "mData": "summary", "sWidth": "50%" },
            { "mData": "firstTime" },
            { "mData": "lastTime" },
        ],
        "aaSorting": [[ 0, "desc" ]],
    } );
} );
