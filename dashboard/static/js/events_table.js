$(document).ready(function () {
    $('#events').dataTable({
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
        "aoColumns": [
            { "mData": "severity", "bVisible": false },
            { "mData": "count" },
            { "mData": "firstTime" },
            { "mData": "component.text" },
            { "mData": "summary" },
            { "mData": "eventState" },
            { "mData": "device.text" },
            { "mData": "eventClass.text" },
            { "mData": "lastTime" },
        ],
        "aaSorting": [[ 0, "desc" ]],
    } );

/*    $.fn.dataTableExt.afnFiltering.push(
            function(oSettings, aData, iDataIndex){
                var row = oSettings.aoData[iDataIndex].nTr,
                    show = $(".toggle-row-display .selected").data("show"),
                    status = +$(row).data("action_approved");

                if (show === "all"){
                    return true;
                } else if (show === "Acknowledged") {
                    return (status === 1);
                } else if (show === "New")
                */
} );
