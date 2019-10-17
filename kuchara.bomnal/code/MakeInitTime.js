console = require('console');
dates = require('dates');

module.exports.function = function makeInitTime (dateTimeExpression) {

  // let response = {
  //   'date': {
  //     'year': 2019,
  //     'month': 10,
  //     'day': 16,
  //     // 'fuzzyFactor': 
  //   },
  //   //'dateTime': {},
  //   //'dateInterval': {},
  //   //'dateTimeInterval': {}
  // }
  // if(typeof dateTimeExpression.date.year == 'undefined') {
  //   response.date.year = 2020
  // }

  let response = {
    'year': 2019,
    'month': 10,
    'day': 20
  }

  console.log(typeof dateTimeEpxression)
  // console.log(typeof dateTimeExpression.date.year)

  return response
}
