#!/usr/bin/node
const { argv } = require('process');
const number = parseInt(argv[2]);

const answer = factorial(number);

function factorial (n) {
    /* if(n < 0){
        return "number has to be positive."
    } */
    
    //base case
    if(n == 0 || n == 1){
        return 1;
    //recursive case
    }else{
        return n * factorial(n-1);
    }
}

console.log(answer);
