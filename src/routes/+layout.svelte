<script>
    import "../app.pcss";
    import { FirebaseApp } from "sveltefire";

    import { auth, firestore } from "$lib/firebase/firebase";
</script>

<FirebaseApp {auth} {firestore}>
    <slot />
</FirebaseApp>
