<<<<<<< HEAD
/*global django:true, jQuery:false*/
=======
>>>>>>> 5cf4e93396b90faed393a6bcb4180d63eb23a5d9
/* Puts the included jQuery into our own namespace using noConflict and passing
 * it 'true'. This ensures that the included jQuery doesn't pollute the global
 * namespace (i.e. this preserves pre-existing values for both window.$ and
 * window.jQuery).
 */
var django = django || {};
django.jQuery = jQuery.noConflict(true);
