console = require('console');
dates = require('dates');

module.exports.function = function findWeekday (dateTimeExpression, actor) {
  console.log(dateTimeExpression.dateTime.date.year);
  console.log(dateTimeExpression.dateTime.date.month);
  console.log(dateTimeExpression.dateTime.date.day);

  if(typeof dateTimeExpression.dateTime.time != 'undefined') {
    console.log(dateTimeExpression.dateTime.time.hour);
    console.log(dateTimeExpression.dateTime.time.minute);
    console.log(dateTimeExpression.dateTime.time.second);
  }
}
