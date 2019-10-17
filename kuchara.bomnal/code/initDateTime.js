dates = require('dates');

module.exports.function = function initDate () {
  let zonedDateTime = new dates.ZonedDateTime('Asia/Seoul')

  response = {
    'year': zonedDateTime.getYear(),
    'month': zonedDateTime.getMonth(),
    'day': zonedDateTime.getDay()
  }

  return response;
}
