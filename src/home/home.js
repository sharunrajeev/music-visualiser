import "./home.css";

const Home = () => {
    return (
        <section class="home-section">
            <h1 class="main-heading">Music Equiliser</h1>
            <form class="upload-form" action="http://localhost:5000/music" method="post" enctype="multipart/form-data">
                <label>Upload your audio file</label>
                <div class="audio-input">
                    <input class="form-input" type="file" accept="audio/*" name="file" required></input>
                    <button class="btn" type="submit">Upload</button>
                </div>
            </form>
            <div class="download">
                <label>Click to download</label>
                <div>
                    <button class="btn">Download</button>
                </div>
            </div>
        </section>
    )
}

export default Home;