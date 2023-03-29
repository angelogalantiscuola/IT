# use_JS_code_from_another_file.md

## How to use JavaScript function from another file

Another way is to make sure that the function is defined in the **global scope** or in a scope that is accessible by the other file. You also need to load the file that defines the function **before** the file that calls it. For example, you can define the function in first.js like this:

```javascript
function fn1 () {
  alert ("external fn clicked");
}
```

And then call it in second.js like this:

```javascript
document.getElementById ("btn").onclick = function () {
  fn1 ();
}
```

But you need to load first.js before second.js in your HTML file like this:

```html
<script type="text/javascript" src="first.js"></script>
<script type="text/javascript" src="second.js"></script>
```

## How to use JavaScript class from another file

To use a JavaScript class from another file, you need to **export** the class from the file where it is defined and **import** it in the file where you want to use it. There are two ways to export and import classes: using the **default** keyword or using the **named** keyword.

If you use the default keyword, you can export only one class per file and you don’t need to use curly braces when importing it. For example, if you have a file called `Person.js` that defines a class called `Person`, you can export it like this:

```javascript
// Person.js
export default class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  greet() {
    console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
  }
}
```

And then import it in another file like this:

```javascript
// Main.js
import Person from './Person.js'; // no need for curly braces or .js extension

let alice = new Person('Alice', 25);
alice.greet(); // Hello, my name is Alice and I am 25 years old.
```

If you use the named keyword, you can export multiple classes per file and you need to use curly braces when importing them. For example, if you have a file called `Animals.js` that defines two classes called `Dog` and `Cat`, you can export them like this:

```javascript
// Animals.js
export class Dog {
  constructor(name) {
    this.name = name;
  }
  bark() {
    console.log(`${this.name} says woof!`);
  }
}

export class Cat {
  constructor(name) {
    this.name = name;
  }
  meow() {
    console.log(`${this.name} says meow!`);
  }
}
```

And then import them in another file like this:

```javascript
// Main.js
import {Dog, Cat} from './Animals.js'; // need curly braces and .js extension

let fido = new Dog('Fido');
fido.bark(); // Fido says woof!

let fluffy = new Cat('Fluffy');
fluffy.meow(); // Fluffy says meow!
```

To use JavaScript classes from other files, you need to use the `<script>` tag with the `type="module"` attribute in your HTML file. This tells the browser that the script is a JavaScript module that can use the `import` and `export` syntax to load and export classes from other files. For example, if you have a file called `main.js` that imports a class called `Person` from another file called `Person.js`, you can link it to your HTML file like this:

```html
<script type="module" src="main.js"></script>
```
