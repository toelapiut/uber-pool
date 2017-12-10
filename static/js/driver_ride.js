$(document)
    .ready(function () {
        $('button#driver')
            .click(function () {
                select = {
                    'Driver':1
                }
                console.log(select)
                alert('sddsds')
                $.ajax({
                    'url': '/ajax/driver/rider/',
                    'type': 'POST',
                    'data': select,
                    'dataType': 'json',
                    'success': function (data) {
                        alert(data['success'])
                    }
                })
            })
            $('button#rider')
            .click(function () {
                select= {
                    'Rider':2
                }
                console.log(select)
                alert('sddsds')
                $.ajax({
                    'url': '/ajax/driver/rider/',
                    'type': 'POST',
                    'data': select,
                    'dataType': 'json',
                    'success': function (data) {
                        alert(data['success'])
                    }
                })
            })
    });