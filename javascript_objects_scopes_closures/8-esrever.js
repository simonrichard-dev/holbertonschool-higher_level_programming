#!/usr/bin/node
exports.esrever = function (list) {
  const li = [];
  for (let i = list.length; i > 0; i--) {
    li.push(list[i - 1]);
  }
  return (li);
};
