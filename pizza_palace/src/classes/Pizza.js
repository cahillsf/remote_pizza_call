import React from 'react';

export default class Pizza {
  // constructor({size = 'medium', toppings = 'default toppings value'} = {size:'medium', toppings:'default option toppings'})
  constructor(size = 'medium', toppings = 'default toppings value')  
  // constructor(size, toppings) 
  {
    this.size = size;
    this.toppings = toppings;
  }

  get size(){
    // return this._size;
    return this.size;
  }

  set size(newSize){
    // this._size = newSize;
    this.size = newSize;
  }

  get toppings(){
    return this._toppings;
  }

  set toppings(newToppings){
    this._toppings = newToppings;
  }

}