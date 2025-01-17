/* eslint-disable no-unused-vars */
import { Layout, Typography, Row, Col, Divider, Image } from "antd";
const { Content } = Layout;
const { Paragraph } = Typography;

import Main_repo from "/Images/github/Main_repo.png";
import Issues from "/Images/github/Issues.png";
import PullRequest from "/Images/github/PullRequest.png";
import Template from "/Images/github/Template.png";
import { ImageCap } from "../../components/ImageCap";

export default function GitHub() {
  return (
    <>
      <h1>GitHub</h1>
      <h1 style={{ marginBottom: "32px", fontSize: "1.5vmax" }}>
        Project Structure
      </h1>
      <Paragraph className="SE" style={{ lineHeight: "36px" }}>
        Prior to commencing the project, we recognized the importance of
        establishing a well-structured repository from the outset. To kickstart
        our own project, we opted to adopt the project structure employed by the
        Three.js repository. In addition to this foundational structure, we
        introduced an additional folder named 'examples.' This dedicated section
        is designed to assist future developers joining the project, providing
        them with an opportunity to familiarize themselves with the codebase.
        The 'examples' folder serves as a valuable resource for developers
        looking to explore each component independently, accompanied by detailed
        explanations in the code. This facilitates a smoother onboarding
        process, allowing new team members to comprehensively understand and
        test individual components within the project.
        <br />
        <ImageCap
          imagesrc={Main_repo}
          description={"Root of the project on GitHub"}
          fignum={1}
        />
      </Paragraph>
      <Divider />
      <h1 style={{ marginBottom: "32px", fontSize: "1.5vmax" }}>
        Best Practices
      </h1>
      <Paragraph className="SE">
        From day one, we embraced GitHub best practices, leveraging templates
        for submitting issues and pull requests (PRs). We integrated GitHub
        Actions to conduct pre-merge code testing, ensuring code stability.
        Future enhancements include implementing custom functions for
        comprehensive testing beyond pylint. Additionally, our commitment to
        transparency involves providing step-by-step documentation with
        screenshots and explanations for every decision made. Comments are
        strategically added to elucidate our thought process, fostering a clear
        understanding of the project's evolution.
        <ImageCap imagesrc={Issues} description={"Issues page"} fignum={2} />
        <br />
        <ImageCap
          imagesrc={PullRequest}
          description={"Pull requests page"}
          fignum={3}
        />
        <br />
        <ImageCap
          imagesrc={Template}
          description={"Issues template"}
          fignum={3}
        />
      </Paragraph>
      <Divider />
    </>
  );
}
