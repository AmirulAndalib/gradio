<script lang="ts">
	import { createEventDispatcher } from "svelte";
	import { copy } from "@gradio/utils";

	import MarkdownCode from "./MarkdownCode.svelte";

	export let elem_classes: string[] = [];
	export let visible = true;
	export let value: string;
	export let min_height = false;
	export let rtl = false;
	export let sanitize_html = true;
	export let line_breaks = false;
	export let latex_delimiters: {
		left: string;
		right: string;
		display: boolean;
	}[];
	export let header_links = false;
	export let height: number | string | undefined = undefined;

	const dispatch = createEventDispatcher<{ change: undefined }>();

	const css_units = (dimension_value: string | number): string => {
		return typeof dimension_value === "number"
			? dimension_value + "px"
			: dimension_value;
	};

	$: value, dispatch("change");
</script>

<div
	class:min={min_height}
	class="prose {elem_classes.join(' ')}"
	class:hide={!visible}
	data-testid="markdown"
	dir={rtl ? "rtl" : "ltr"}
	use:copy
	style={height ? `max-height: ${css_units(height)}; overflow-y: auto;` : ""}
>
	<MarkdownCode
		message={value}
		{latex_delimiters}
		{sanitize_html}
		{line_breaks}
		chatbot={false}
		{header_links}
	/>
</div>

<style>
	div :global(.math.inline) {
		fill: var(--body-text-color);
		display: inline-block;
		vertical-align: middle;
		padding: var(--size-1-5) -var(--size-1);
		color: var(--body-text-color);
	}

	div :global(.math.inline svg) {
		display: inline;
		margin-bottom: 0.22em;
	}

	div {
		max-width: 100%;
	}

	.min {
		min-height: var(--size-24);
	}
	.hide {
		display: none;
	}
</style>
