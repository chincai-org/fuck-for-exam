<script lang="ts">
    export let title: any;
    export let id: any;
</script>

<a data-sveltekit-reload href={window.location.href + "/" + id}>{title}</a>

<style lang="sass">
    a
        background-color: black
        color: white
</style>
