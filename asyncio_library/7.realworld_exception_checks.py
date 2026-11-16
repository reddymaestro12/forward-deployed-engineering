import asyncio

async def retrieve_from_faiss():
    await asyncio.sleep(1)
    return ["doc1", "doc2"]

async def retrieve_from_bm25():
    await asyncio.sleep(1)
    raise ConnectionError("BM25 service unavailable")

async def retrieve_from_web():
    await asyncio.sleep(1)
    return ["web_doc1"]

async def main():
    results = await asyncio.gather(
        retrieve_from_faiss(),
        retrieve_from_bm25(),
        retrieve_from_web(),
        return_exceptions=True
    )

    documents = []

    for result in results:
        if isinstance(result, Exception):
            print(f"Retriever failed: {result}")
        else:
            documents.extend(result)

    print("Final documents:", documents)

asyncio.run(main())