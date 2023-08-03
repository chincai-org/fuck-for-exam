<script lang="ts">
    export let button: any;
</script>

<a href={window.location.href + "/" + button.route}>{button.title}</a>
