/*global define*/
define([], function () {
    $("#filter-table thead th.filter").each(function () {
        var title = $(this).text();
        $(this).append("<input type='text' placeholder='' style='width: 100%;' class='form-control input-sm' />");
    });

    var table = default_data_table();

    decorate_man_list_inputs();

    align_filter();

    table_column_search(table);
});