<script>
    import "../app.pcss";
    import { FirebaseApp } from "sveltefire";
    import "/src/lib/sass/main.scss";
    import "@fortawesome/fontawesome-free/css/all.min.css";
    import { auth, firestore } from "$lib/firebase/firebase";
</script>

<FirebaseApp {auth} {firestore}>
    <slot />
</FirebaseApp>
