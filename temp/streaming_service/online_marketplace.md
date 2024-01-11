# Online Marketplace

1. We have a `Customer` who can make `Orders`. The `Customer` has a `username`, `email`, and can also create multiple `Wishlists`.

2. There's a `Seller` who can list multiple `Products`. The `Seller` has a `name` and `rating`.

3. Each `Product` can belong to multiple `Categories` and is listed by a `Seller`. The `Product` has a `title`, `description`, `price`, and `stockQuantity`. There's also a special type of `Product`, called `PremiumProduct`, that comes with `extraFeatures`.

4. Each `Category` can contain multiple `Products` and has a `name`.

5. A `Wishlist` belongs to a `Customer` and can contain multiple `Products`. The `Wishlist` has a `name`.

6. An `Order` is associated with a `Customer` and can contain multiple `OrderItems`. The `Order` has an `orderNumber`, `orderDate`, and `status`.

7. Each `OrderItem` is associated with a `Product` and belongs to an `Order`. The `OrderItem` has a `quantity` and `price`.

8. A `Review` is associated with a `Product` and written by a `Customer`. The `Review` has a `rating` and `comment`.

9. A `ShippingAddress` is associated with an `Order`. The `ShippingAddress` has `street`, `city`, `state`, `country`, and `zipCode`.

10. A `Payment` is associated with an `Order`. The `Payment` has a `paymentMethod`, `amount`, and `paymentDate`.

Remember to use the correct PlantUML syntax for defining classes, attributes, relationships, and inheritance.