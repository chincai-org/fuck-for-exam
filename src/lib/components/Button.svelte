<script lang="ts">
    export let button: any;
    export let clicked: (event: any) => void;
</script>

<button on:click={clicked}>{button.title}</button>

<style lang="sass">
    button
        background-color: black
        color: white
</style>
