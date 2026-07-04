// 1. Slice out the surrounding quotes from Django's json_script tags
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);

// 2. Initialize the Stripe secure tunnel instance
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

// 3. Define the style object FIRST
var style = {
    base: {
        color: '#ffffff', 
        fontFamily: '"Courier New", Courier, monospace', 
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#6c757d'
        },
        ':-webkit-autofill': {
            color: '#ffffff',
        }
    },
    invalid: {
        color: '#dc3545', 
        iconColor: '#dc3545'
    }
};

// 4. Create the card element passing the style object SECOND
var card = elements.create('card', {
    style: style,
    hidePostalCode: true
});

// 5. Mount it to the HTML layout THIRD
card.mount('#card-element');