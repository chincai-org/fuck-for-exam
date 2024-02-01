<script lang="ts">
    export let timeInMilliseconds: number;
    export let score: number;

    // Convert time to minutes and seconds
    const minutes = Math.floor(timeInMilliseconds / 60000);
    const seconds = Math.floor((timeInMilliseconds % 60000) / 1000);
</script>

<p>Time used: {minutes.toString().padStart(2, "0")}:{seconds.toString().padStart(2, "0")}</p>
<p>Score: {(score * 100).toFixed(2)}</p>
